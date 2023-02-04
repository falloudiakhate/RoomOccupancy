
from django.core.cache import cache
from django.test import RequestFactory, TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from API.views import *

class WebhookListenerTestCase(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_webhook_listener_success(self):
        # Arrange
        url = '/api/webhook_listener/'
        request_data = {'sensor': 'abc', 'ts': '2022-01-01T01:00:00', 'in_count': 1, 'out_count': 0}
        request = self.factory.post(url, request_data, content_type='application/json')
        
        # Act
        response = webhook_listener(request)
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Data added successfully', 'ts': '2022-01-01T01:00:00'})

    def test_webhook_listener_failure(self):
        # Arrange
        url = '/api/webhook_listener/'
        request_data = {'ts': '2022-01-01T01:00:00', 'in_count': 1, 'out_count': 0}
        request = self.factory.post(url, request_data, content_type='application/json')
        
        # Act
        response = webhook_listener(request)
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
        

class GetOccupancyTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        #Clean cache
        cache.clear()
        # Create some mock sensor data in cache
        self.sensor = 'abc'
        cache.set(self.sensor, {
            '2018-11-14T14:00:00Z': {'in_count': 9, 'out_count': 3},
            '2018-11-14T15:00:00Z': {'in_count': 7, 'out_count': 5},
        })

    def test_get_occupancy_at_instant(self):
        request = self.factory.get('/sensors/abc/occupancy', {'atInstant': '2018-11-14T14:00:00Z'})
        response = get_occupancy(request, self.sensor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'inside': 6})

    def test_get_occupancy_current(self):
        request = self.factory.get('/sensors/abc/occupancy')
        response = get_occupancy(request, self.sensor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'sensor': 'abc', 'inside': 8})

    def test_get_occupancy_sensor_not_found(self):
        request = self.factory.get('/sensors/xyz/occupancy')
        response = get_occupancy(request, 'xyz')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'error': 'Sensor not found'})
        
    


class GetSensorsTestCase(TestCase):
    def test_get_sensors(self):
        #Clean cache
        cache.clear()
        # Add some sensor keys to the cache
        cache.set("sensors:abc", 1)
        cache.set("sensors:def", 2)
        cache.set("sensors:ghi", 3)
        
        # Make a GET request to the get_sensors endpoint
        url = reverse('get_sensors')
        response = self.client.get(url)
        
        # Assert that the response has a status code of 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the response contains a list of sensors
        self.assertEqual(response.data, {'sensors': ['ghi', 'def', 'abc']})
        
     



