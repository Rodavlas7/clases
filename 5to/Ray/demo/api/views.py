from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.serializers import UserSerializer

from django.contrib.auth.models import User

# Create your views here.

class UserListApiVIew(APIView):
    def get(self, request):
        queryset = User.objects.all()
        data = UserSerializer(queryset, many = True).data
        return Response(data)