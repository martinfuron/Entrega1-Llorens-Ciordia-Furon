from django.contrib import admin
from django.urls import path, include
from Blog.views import mostrar_inicio, mostrar_articulos, mostrar_autores, mostrar_seccion, procesar_formulario

urlpatterns = [
    path("inicio/",mostrar_inicio),
    path("autor/",mostrar_autores),
    path("articulo/",mostrar_articulos),
    path("seccion/",mostrar_seccion),
    path ("formularioautor/", procesar_formulario, name="formularioautor")
]