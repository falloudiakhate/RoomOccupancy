# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ObservationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from rest_framework import status


@api_view(['POST'])
@csrf_exempt
def webhook_listener(request):
    # Deserialize the incoming data
    serializer = ObservationSerializer(data=request.data)

    # Validate the incoming data
    if serializer.is_valid():
        # Store the validated data in memory
        sensor = serializer.validated_data['sensor']
        ts = serializer.validated_data['ts']
        in_count = serializer.validated_data['in_count']
        out_count = serializer.validated_data['out_count']
        
        # Add the validated data to the in-memory occupancy data
        # Check if sensor data already exists in cache
        sensor_data = cache.get(sensor)
        
        if sensor_data:
            # Update the data in cache
            if ts in sensor_data:
                sensor_data[ts]['in_count'] += in_count
                sensor_data[ts]['out_count'] += out_count
            else:
                sensor_data[ts] = {'in_count': in_count, 'out_count': out_count}
        else:
            # Add new data to cache
            sensor_data = {ts: {'in_count': in_count, 'out_count': out_count}}

        # Store the updated data in cache
        cache.set(sensor, sensor_data)
    
        # Return a success response
        return Response({'message': 'Data added successfully', 'ts' : ts}, status=status.HTTP_200_OK)
    else:
        # Return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
@api_view(['GET'])    
def get_occupancy(request, sensor):
    at_instant = request.GET.get('atInstant')
    # Get the occupancy data for a particular sensor
    sensor_data = cache.get(sensor)
    if sensor_data:
        if at_instant:
            occupancy = sensor_data.get(at_instant, {}).get('in_count', 0) - sensor_data.get(at_instant, {}).get('out_count', 0)
            return Response({'inside': occupancy})
        else:
            # Calculate the current occupancy
            occupancy = sum([data.get('in_count', 0) for data in sensor_data.values()]) - sum([data.get('out_count', 0) for data in sensor_data.values()])
            return Response({'sensor' : sensor , 'inside': occupancy}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Sensor not found'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_sensors(request):
    # Get the list of sensor keys from cache
    sensor_keys = cache._cache.keys()
    # Remove the prefix from the sensor keys
    sensors = [key.split(":")[-1] for key in sensor_keys]
    # Return the list of sensors
    return Response({'sensors': sensors}, status=status.HTTP_200_OK)

