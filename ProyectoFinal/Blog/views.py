from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Autor, Articulo
from Blog.forms import AutorFormulario, ArticuloFormulario, SeccionFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Blog.forms import AvatarForm, UserEditionForm



def mostrar_inicio(request):    
    return render(request,"blog/inicio.html")

@login_required
def mostrar_autores(request):
    return render(request,"blog/autor.html")

@login_required
def mostrar_articulos(request):
    return render(request,"blog/articulo.html")

@login_required
def mostrar_seccion(request):
    return render(request,"blog/seccion.html")


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
    
    

class BlogList(ListView):
    model = Articulo
    template_name = "Blog\pages.html" 

class BlogDetail(DetailView):
    model = Articulo
    template_name = "Blog\pages.html" 

class BlogCreate(CreateView):
    model = Articulo
    template_name = "Blog\pages.html"

class BlogUpdate(UpdateView):
    model = Articulo
    template_name = "Blog\pages.html" 

class BlogDelete(DeleteView):
    model = Articulo
    template_name = "Blog\pages.html" 

class MyLogin(LoginView):
    template_name = "Blog/login.html"


def login_request(request):

    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "Blog/login.html", {"form": form})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            "Blog/inicio.html",
            {"mensaje": "Error: los datos ingresados no son correctos"},
        )
    else:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(
                request, "Blog/inicio.html", {"mensaje": f"Bienvenido {username}"}
            )
        else:
            return render(
                request,
                "Blog/inicio.html",
                {"mensaje": "El usuario no existe en nuestra appliación"},
            )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/registro.html", {"form": form})