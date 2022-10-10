from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Autor, Articulo, Section

# Create your views here.

def mostrar_inicio(request):    
    return render(request,"blog/inicio.html")

def mostrar_autores(request):
    return render(request,"blog/autor.html")


def mostrar_articulos(request):
    return render(request,"blog/articulo.html")


def mostrar_seccion(request):
    return render(request,"blog/seccion.html")


def procesar_formulario_autor(request):
    if request.method !="POST":
        return render(request, "blog/formulario_autor.html")
    
    autor=Autor ( nombre=request.POST["nombre"],apellido=request.POST["apellido"],profesion=request.POST["profesion"])
    autor.save()
    return render(request,"blog/inicio.html")

def procesar_formulario_articulo(request):
    if request.method !="POST":
        return render(request, "blog/formulario_articulo.html")
    
    autor=Articulo ( titulo=request.POST["titulo"],fecha=request.POST["fecha"],texto=request.POST["texto"])
    autor.save()
    return render(request,"blog/inicio.html")

