from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import SerializerBank
from core.models import Bank

class ListBank(APIView):
    def get(self, request): 
        banks = Bank.objects.all()
        data = SerializerBank(banks, many=True).data
        return Response(data)
    
class DetailBan(APIView):
    def get(self, request, pk):
        bank = Bank.objects.get(pk=pk)
        data = SerializerBank(bank, many=False)
        return Response(data.data)
    
class Update(generics.UpdateAPIView):
    serializer_class = SerializerBank
    queryset = Bank.objects.all()
    lookup_field = "pk"

class Delete(generics.DestroyAPIView):
    serializer_class = SerializerBank
    queryset = Bank.objects.all()
    lookup_field = "pk"

class CreateBank(generics.CreateAPIView):
    serializer_class = SerializerBank

    def perform_create(self, serializer):
        # Toma el primer usuario que exista, o el que esté autenticado
        from django.contrib.auth.models import User
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        serializer.save(user=user)