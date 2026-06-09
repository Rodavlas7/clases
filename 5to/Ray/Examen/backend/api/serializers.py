from rest_framework import serializers
from . import models

class ListGpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GpsDevice
        fields =  'id','brand', 'model', 'is_active'

class CreateGpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GpsDevice
        fields = '__all__'

class DetailGpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GpsDevice
        fields = '__all__'



class ListTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Truck
        fields = 'id', 'plates', 'brand', 'is_active'

class CreateTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Truck
        fields = '__all__'

class DetailTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Truck
        fields = '__all__'