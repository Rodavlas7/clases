from django.db import models

class GpsDevice(models.Model):
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Número de Serie")
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GPS {self.serial_number} - {self.brand}"

class Truck(models.Model):
    economic_number = models.CharField(max_length=20, unique=True, verbose_name="Número Económico")
    plates = models.CharField(max_length=20, unique=True, verbose_name="Placas")
    brand = models.CharField(max_length=50, verbose_name="Marca")
    is_active = models.BooleanField(default=True, verbose_name="¿Está en ruta?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Camión {self.economic_number} ({self.plates})"