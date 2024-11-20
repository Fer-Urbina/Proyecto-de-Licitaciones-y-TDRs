from rest_framework import serializers
from .models import Licitacion, TDR

class LicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacion
        fields = '__all__'  # Serializa todos los campos

class TDRSerializer(serializers.ModelSerializer):
    licitacion = LicitacionSerializer()  # Relación con Licitacion

    class Meta:
        model = TDR
        fields = '__all__'
