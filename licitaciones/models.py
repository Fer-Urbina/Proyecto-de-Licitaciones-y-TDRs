from django.db import models

class Licitacion(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    titulo = models.CharField(max_length=255)  # Título de la licitación
    descripcion = models.TextField()  # Descripción
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_fin = models.DateField()  # Fecha de fin
    estado = models.CharField(max_length=50)  # Estado (Ej., "abierta", "cerrada")

    def __str__(self):
        return self.titulo
    
class TDR(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)  # Relación con licitación
    especificacion = models.TextField()  # Detalle técnico
    prioridad = models.CharField(max_length=50)  # Prioridad (Ej., "alta", "media", "baja")

    def __str__(self):
        return f"TDR de {self.licitacion.titulo} - {self.prioridad}"
