from django.db import models

# Create your models here.

class Autor (models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)


class Articulo (models.Model):
    titulo=models.CharField(max_length=30)
    texto=models.CharField(max_length=1500)
    fecha=models.DateField(null=True)


class Secton (models.Model):
    nombre=models.CharField(max_length=40)