from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Licitacion, TDR
from .serializers import LicitacionSerializer, TDRSerializer

# Create your views here.

class LicitacionListView(APIView):
    def get(self, request):
        licitaciones = Licitacion.objects.all()
        serializer = LicitacionSerializer(licitaciones, many=True)
        return Response(serializer.data)

class TDRListView(APIView):
    def get(self, request):
        tdrs = TDR.objects.all()
        serializer = TDRSerializer(tdrs, many=True)
        return Response(serializer.data)
    
class LicitacionCreateView(APIView):
    def post(self, request):
        serializer = LicitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda el nuevo objeto en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Responde con el nuevo registro
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Responde con errores si no es válido

class LicitacionUpdateView(APIView):
    def put(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk)
        except Licitacion.DoesNotExist:
            return Response({"error": "Licitación no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LicitacionSerializer(licitacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LicitacionDeleteView(APIView):
    def delete(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk)
            licitacion.delete()
            return Response({"message": "Licitación eliminada"}, status=status.HTTP_204_NO_CONTENT)
        except Licitacion.DoesNotExist:
            return Response({"error": "Licitación no encontrada"}, status=status.HTTP_404_NOT_FOUND)


class LicitacionDetailView(APIView):
    def get(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk)
            serializer = LicitacionSerializer(licitacion)
            return Response(serializer.data)
        except Licitacion.DoesNotExist:
            return Response({"error": "Licitación no encontrada"}, status=status.HTTP_404_NOT_FOUND)
