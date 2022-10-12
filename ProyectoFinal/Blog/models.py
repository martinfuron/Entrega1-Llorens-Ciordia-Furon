from django.db import models

# Create your models here.

class Autor (models.Model):
    
    class Meta:
        verbose_name_plural ="Autores"
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)
    
    def __str__(self):
        return (f"{self.nombre} {self.apellido} {self.profesion}")


class Articulo (models.Model):
    
    class Meta:
        verbose_name_plural ="Articulos"
    
    titulo=models.CharField(max_length=30)
    texto=models.TextField(max_length=1500)
    fecha=models.DateField(null=True)

    def __str__(self):
        return (f"{self.titulo} {self.fecha}")



class Section (models.Model):
    
    class Meta:
        verbose_name_plural ="Secciones"
    
    nombre=models.CharField(max_length=40)
    
    def __str__(self):
        return (f"{self.nombre}")
