from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
