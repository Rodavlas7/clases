from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=32, default="No existe")
    level = models.IntegerField(default=1, blank=True, null=True)#Puedes dehar en blanco en nulo o en default
    status = models.BooleanField(default=True)
    weight = models.FloatField(default=2.1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # No cambiar fecha de modificacion Fecha de creacion
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #onetoone
    #manytomany


    def __str__(self):
        return f"{self.name} {self.status}"









