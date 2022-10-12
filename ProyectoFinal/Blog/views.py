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
    
    articulo=Articulo ( titulo=request.POST["titulo"],fecha=request.POST["fecha"],texto=request.POST["texto"])
    articulo.save()
    return render(request,"blog/inicio.html")

def procesar_formulario_seccion(request):
    if request.method !="POST":
        return render(request, "blog/formulario_seccion.html")
    
    seccion=Section ( nombre=request.POST["nombre"])
    seccion.save()
    return render(request,"blog/inicio.html")

def busqueda(request):
    return render(request, "blog/busqueda.html")

def buscar(request):
    if not request.GET("nombre"):
        return HttpResponse("No buscaste nada")
    else:
        nombre = request.GET("nombre")
        autor = Autor.objects.filter(nomnbre=nombre)

        contexto= {
            "nombre": nombre,
            "autor": autor,
        }
    
    return render(request, "blog/resultado_busqueda.html", contexto)

