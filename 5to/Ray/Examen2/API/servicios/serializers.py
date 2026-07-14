from rest_framework import serializers
from django.contrib.auth.models import User
from servicios import models


'''
    class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
'''


class ListaServicio(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = [
            "id",
            "nombre",
            "capacidad",
            "costo",
            "estado"
        ]

class DetalleServicio(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = [
            "id",
            "nombre",
            "capacidad",
            "costo",
            "region",
            "estado"
        ]

class CrearServicio(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = [
            "nombre",
            "capacidad",
            "costo",
            "region",
            "estado"
        ]

class ActualizarServicio(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = [
            "nombre",
            "capacidad",
            "costo",
            "region",
            "estado"
        ]

class EliminarServicio(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = [
            "id"
        ]