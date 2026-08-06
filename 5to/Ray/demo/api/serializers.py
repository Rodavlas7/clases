
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

class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        min_length = 8
    )

    password_confirm =serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirm"
        ]
        read_only_fields = ["id"]

    def validate_username(value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    
    def validate_email(value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate(self, attrs):
        if attrs("password") != attrs("password_confirm"):
            raise serializers.ValidationError({
                "password_confirm": "Passwords do not match"
            })
        return attrs

    def create(self, validated_data):

        validated_data.pop("password_confirm")

        return User.objects.create_user(
            username = validated_data["username"],
            first_name = validated_data.get["first_name", ""],
            last_name = validated_data.get["last_name", ""],
            email = validated_data.get["email", ""],
            password = validated_data["password"]
        )