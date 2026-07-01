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
class UpdateBankSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Bank
        fields = [
            "name",
            "address",
            "status"
        ]

## delete serializer
class DeleteBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            "id",
        ]

## Accounts serializers

## List
class ListAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = [
            "id",
            "name",
            "bank",
            "status"
        ]

class DetailAccountSerializer(serializers.ModelSerializer):
    bank = DetailBankSerializer()
    user = UserSerializer()

    class Meta:
        model = models.Account
        fields = "__all__"

##payment serializers

class PaymentSerializer(serializers.ModelSerializer):
    accounts_detail = DetailAccountSerializer(source='accounts', many=True, read_only=True)
    user_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = models.Payment
        fields = [
            "id",
            "name",
            "accounts",
            "accounts_detail",
            "created_by",
            "user_name",
            "created_at"
        ]

class ListPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            "id",
            "name",
            "created_by",
            "created_at"
        ]

class DetailPaymentSerializer(serializers.ModelSerializer):
    accounts_detail = DetailAccountSerializer(source='accounts', many=True, read_only=True)
    user_name = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = models.Payment
        fields = [
            "id",
            "name",
            "accounts",
            "accounts_detail",
            "created_by",
            "user_name",
            "created_at"
        ]

class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            "name",
            "accounts",
            "created_by"
        ]