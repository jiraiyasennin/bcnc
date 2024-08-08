from django.db import models
from django.contrib.auth.models import User

class Vivienda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viviendas')
    direccion = models.CharField(max_length=255)
    calle = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo
    ciudad = models.CharField(max_length=100)  # Nuevo campo
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo
    codigo_postal = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.direccion}, {self.ciudad}, {self.pais} - {self.usuario.username}'
