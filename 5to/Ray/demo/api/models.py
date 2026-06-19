from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    name = models.CharField(default='Generic Bank Name',max_length=32)
    address = models.CharField(default='Generic Bank Address',max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
CHOICES = (
    ('Dolar Americano','USD'),
    ('Peso Mexicano','MXN'),
    ('EURO','EUR'),
)
class Account(models.Model):
    name = models.CharField(default='Generic Account Name',max_length=32)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency = models.CharField(default='USD',max_length=16, choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    name = models.CharField(verbose_name='Nombre del pago',max_length=50)
    accounts = models.ManyToManyField(Account, verbose_name='Cuentas', related_name='payments')
    created_by = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name