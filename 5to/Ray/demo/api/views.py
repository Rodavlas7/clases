from api import models
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from api import serializers

from django.contrib.auth.models import User

# Create your views here.

class UserListApiVIew(APIView):
    def get(self, request):
        queryset = User.objects.all()
        data = serializers.UserSerializer(queryset, many = True).data
        return Response(data)
    
class ListBankApiView(APIView):
    def get(self, request):
        queryset = models.Bank.objects.all()
        data = serializers.ListBankSerializer(queryset, many = True).data
        return Response(data)
    
class DetailBankApiView(APIView):
    def get(self, request, pk):
        queryset = models.Bank.objects.get(id = pk)
        data = serializers.DetailBankSerializer(queryset, many=False).data
        return Response(data)
    
class CreateBankApiView(generics.CreateAPIView):
    serializer_class = serializers.CreateBankSerializer
    
class UpdateBankApiView(generics.UpdateAPIView):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.UpdateBankSerializer

class DeleteBankApiView(generics.DestroyAPIView):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.DeleteBankSerializer

class ListAccountApiView(generics.ListAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.ListAccountSerializer

class DetailAccountApiView(generics.RetrieveAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.DetailAccountSerializer

## account vieww

class ListPaymentApiView(generics.ListAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class DetailPaymentApiView(generics.RetrieveAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.DetailPaymentSerializer