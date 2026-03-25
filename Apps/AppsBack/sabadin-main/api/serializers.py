from rest_framework import serializers
from core.models import Bank

class SerializerBank(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        read_only_fields = ['user']  # Flutter no lo envía, Django lo asigna