from rest_framework import generics
from . import models
from . import serializers


# ENDPOINTS GPS

class ListGpsApiView(generics.ListAPIView):
    queryset = models.GpsDevice.objects.all()
    serializer_class = serializers.ListGpsSerializer

class CreateGpsApiView(generics.CreateAPIView):
    queryset = models.GpsDevice.objects.all()
    serializer_class = serializers.CreateGpsSerializer

class DetailGpsApiView(generics.RetrieveAPIView):
    queryset = models.GpsDevice.objects.all()
    serializer_class = serializers.DetailGpsSerializer


# ENDPOINTS CAMIONES

class ListTruckApiView(generics.ListAPIView):
    queryset = models.Truck.objects.all()
    serializer_class = serializers.ListTruckSerializer

class CreateTruckApiView(generics.CreateAPIView):
    queryset = models.Truck.objects.all()
    serializer_class = serializers.CreateTruckSerializer

class DetailTruckApiView(generics.RetrieveAPIView):
    queryset = models.Truck.objects.all()
    serializer_class = serializers.DetailTruckSerializer