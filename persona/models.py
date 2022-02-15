import email
from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20)
    lugar_residencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_nacimiento = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
