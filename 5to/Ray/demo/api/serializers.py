from rest_framework import serializers
from django.contrib.auth.models import User
from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]

## Banks serializers

## Create serializer bank
class CreateBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "name",
            "address",
        ]

## list and detail serializer bank
class ListBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "id",
            "name",
            "status"
        ]

class DetailBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "id",
            "name",
            "address",
            "timestamp",
            "updated",
            "status",
        ]

## update serializer bank 
# CAMBIADO: Nombre único para evitar sobrescribir el anterior
class UpdateBankSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Bank
        fields = [
            "name",
            "address", # CORREGIDO: doble 'd'
            "status"
        ]

## delete serializer
class DeleteBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "id",
        ]