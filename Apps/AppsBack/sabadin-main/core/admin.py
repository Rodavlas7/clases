from django.contrib import admin
from .models import Bank #Mismo folder .

# Register your models here.
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "timestamp",
        "updated",
        "user"
    ]

#REGISTRAR TABñas