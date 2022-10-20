from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Autor, Articulo, Section
from Blog.forms import AutorFormulario, ArticuloFormulario, SeccionFormulario

# Create your views here.

def mostrar_inicio(request):    
    return render(request,"blog/inicio.html")

def mostrar_autores(request):
    return render(request,"blog/autor.html")

def mostrar_articulos(request):
    return render(request,"blog/articulo.html")

def mostrar_seccion(request):
    return render(request,"blog/seccion.html")


    if request.method !="POST":
        return render(request, "blog/formulario_autor.html")
    
    autor=Autor ( nombre=request.POST["nombre"],apellido=request.POST["apellido"],profesion=request.POST["profesion"])
    autor.save()
    return render(request,"blog/inicio.html")

def formulario_autor(request):
    if request.method != "POST":
        mi_formulario = AutorFormulario()
    else:
        mi_formulario = AutorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            autor=Autor ( nombre=informacion["nombre"],apellido=informacion["apellido"],profesion=informacion["profesion"])
            autor.save()
            return render(request,"blog/inicio.html")
            
    contexto =  {"formulario": mi_formulario}
    return render(request, "Blog/formulario.html", contexto)


    if request.method !="POST":
        return render(request, "blog/formulario_articulo.html")
    
    articulo=Articulo ( titulo=request.POST["titulo"],fecha=request.POST["fecha"],texto=request.POST["texto"])
    articulo.save()
    return render(request,"blog/inicio.html")

def formulario_articulo(request):
    if request.method !="POST":
        return render(request, "blog/formulario_articulo.html")
    
    articulo = Articulo( titulo=request.POST["titulo"],fecha=request.POST["fecha"],texto=request.POST["texto"])
    articulo.save()
    return render(request,"blog/inicio.html")    

def formulario_seccion(request):
    if request.method != "POST":
        mi_formulario = SeccionFormulario()
    else:
        mi_formulario = SeccionFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            seccion = Section( nombre=informacion["nombre"])
            seccion.save()
            return render(request,"blog/inicio.html")
            
    contexto =  {"formulario": mi_formulario}
    return render(request, "Blog/formulario.html", contexto)

def busqueda(request):
    return render(request, "blog/busqueda.html")

def buscar (request):

    if not request.GET["apellido"]:
        return HttpResponse ("No se enviaron datos")
    else: 
        apellido_buscado= request.GET["apellido"]
        autores = Autor.objects.filter(apellido = apellido_buscado)
                
        contexto={
            "apellido": apellido_buscado,
             "autores": autores
             }
    
    return render(request, "blog/resultado_busqueda.html", contexto)


def mostrar_articulos (request):  
    articulos = Articulo.objects.all()
                
    contexto={
             "articulos": articulos,
             }
    return render(request, "blog/articulo.html", contexto)