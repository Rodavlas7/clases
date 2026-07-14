from servicios import models
from servicios import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class ListServicioApiView(APIView):
    serializer_class = serializers.ListaServicio

    def get(self, request):
        queryset = models.Servicio.objects.all()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)




class CreateServicioApiView(APIView):
    serializer_class = serializers.CrearServicio  

    def get(self, request):
        return Response()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DetailServicioApiView(APIView):
    serializer_class = serializers.DetalleServicio

    def get(self, request, pk):
        try:
            servicio = models.Servicio.objects.get(id=pk)
        except models.Servicio.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        data = self.serializer_class(servicio).data
        return Response(data)


class UpdateServicioApiView(APIView):
    serializer_class = serializers.ActualizarServicio  

    def get(self, request, pk):
        try:
            servicio = models.Servicio.objects.get(id=pk)
        except models.Servicio.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(servicio)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            servicio = models.Servicio.objects.get(id=pk)
        except models.Servicio.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteServicioApiView(APIView):
    serializer_class = serializers.EliminarServicio

    def delete(self, request, pk):
        try:
            servicio = models.Servicio.objects.get(id=pk)
        except models.Servicio.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)