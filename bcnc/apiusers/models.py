from django.db import models
from django.contrib.auth.models import User


class Vivienda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viviendas')
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.direccion}, {self.ciudad} - {self.usuario.username}'
