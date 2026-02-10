from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=255)
    edad = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return self.nombre