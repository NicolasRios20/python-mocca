from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Experiencia(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='experiencias/imagenes/')
    url = URLField(blank=True)
    
class Servicios(models.Model):
    servicio = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=250)
    capacidad = models.IntegerField()  # Corregido: models.IntegerField en vez de IntegerField de forms
    aire_acondicionado = models.BooleanField(default=True)  # Corregido: models.BooleanField en vez de BooleanField de forms
    reclinable = models.BooleanField(default=True)  # Corregido: models.BooleanField en vez de BooleanField de forms
    imagen = models.ImageField(upload_to='servicios/imagenes/')
