from django.db import models

# Create your models here.
class Campeon(models.Model):
    """
    Modelo que representa la estructura de 
    datos de un pokemon en base de datos
    """
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    dificultad = models.CharField(max_length=200)
    imagen = models.FileField(upload_to="campeones/")

    def __str__(self):
        return self.nombre