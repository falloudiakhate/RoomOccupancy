from rest_framework import serializers

class ObservationSerializer(serializers.Serializer):
    sensor = serializers.CharField()
    ts = serializers.CharField()
    in_count = serializers.IntegerField()
    out_count = serializers.IntegerField()
