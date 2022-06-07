from tkinter import commondialog
from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.CharField(max_length=250)