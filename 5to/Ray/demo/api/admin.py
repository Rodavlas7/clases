from django.contrib import admin
from api import models

# Register your models here.

@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "timestamp",
        ]

@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "bank",
        "status"
    ]

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_by",
        "created_at"
    ]