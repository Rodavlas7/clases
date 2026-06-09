from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from api import models
from api import serializers


# VISTAS PARA DISPOSITIVOS GPS

class ListGpsApiView(APIView):
    def get(self, request):
        queryset = models.GpsDevice.objects.all()
        data = serializers.ListGpsSerializer(queryset, many=True).data
        return Response(data)
    
class DetailGpsApiView(APIView):
    def get(self, request, pk):
        queryset = models.GpsDevice.objects.get(id=pk)
        data = serializers.DetailGpsSerializer(queryset, many=False).data
        return Response(data)
    
class CreateGpsApiView(generics.CreateAPIView):
    serializer_class = serializers.CreateGpsSerializer


# VISTAS PARA CAMIONES (TRUCKS)

class ListTruckApiView(APIView):
    def get(self, request):
        queryset = models.Truck.objects.all()
        data = serializers.ListTruckSerializer(queryset, many=True).data
        return Response(data)
    
class DetailTruckApiView(APIView):
    def get(self, request, pk):
        queryset = models.Truck.objects.get(id=pk)
        data = serializers.DetailTruckSerializer(queryset, many=False).data
        return Response(data)
    
class CreateTruckApiView(generics.CreateAPIView):
    serializer_class = serializers.CreateTruckSerializer