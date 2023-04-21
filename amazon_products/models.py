from django.db import models

# Create your models here.
class Producto(models.Model):
    fecha = models.DateField()
    imagen = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    distribuidor = models.CharField(max_length=255)
    ASIN = models.CharField(max_length=255)
    precio = models.FloatField()
    EAN = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre