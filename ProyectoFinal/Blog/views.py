from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mostrar_inicio(request):    
    return render(request,"Blog/inicio.html")

def mostrar_autores(request):
    return render(request,"Blog/autor.html")


def mostrar_articulos(request):
    return render(request,"Blog/articulo.html")


def mostrar_seccion(request):
    return render(request,"Blog/seccion.html")