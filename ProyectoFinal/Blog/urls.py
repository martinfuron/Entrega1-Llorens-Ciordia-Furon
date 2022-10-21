from django.contrib import admin
from django.urls import path 
from django.shortcuts import redirect
from Blog.views import (
        mostrar_inicio, mostrar_articulos, mostrar_autores, mostrar_seccion,
        busqueda, buscar, formulario_autor, 
        formulario_articulo, formulario_seccion
      )


urlpatterns = [
    path('', lambda req: redirect('/blog/inicio/')),
    path("inicio/",mostrar_inicio),
    path("autor/",mostrar_autores),
    path("articulo/",mostrar_articulos),
    path("seccion/",mostrar_seccion),
    path ("formulario_autor/", formulario_autor, name="formulario_autor"),
    path ("formulario_articulo/", formulario_articulo, name="formulario_articulo"),
    path ("formulario_seccion/", formulario_seccion, name="formulario_seccion"),
    path ("buscar/",  buscar),
    path ("busqueda/", busqueda, name="busqueda")
    

    ]   