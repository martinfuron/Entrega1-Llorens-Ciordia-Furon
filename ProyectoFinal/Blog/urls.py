from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from Blog.views import  (
    mostrar_inicio, 
    mostrar_autores, 
    mostrar_articulos, 
    mostrar_seccion, 
    procesar_formulario_articulo, 
    procesar_formulario_autor,
    procesar_formulario_seccion,
    busqueda,
    buscar
)
=======
from Blog.views import mostrar_inicio, mostrar_articulos, mostrar_autores, mostrar_seccion, procesar_formulario_autor, procesar_formulario_articulo
>>>>>>> 0d4f3f5489f92a7c36a52595a1679bdb12d832c3

urlpatterns = [
    path("inicio/",mostrar_inicio),
    path("autor/",mostrar_autores),
    path("articulo/",mostrar_articulos),
    path("seccion/",mostrar_seccion),
    path ("formulario_autor/", procesar_formulario_autor, name="formulario_autor"),
<<<<<<< HEAD
    path ("formulario_articulo/", procesar_formulario_articulo, name="formulario_articulo"),
    path("formulario_seccion/",procesar_formulario_seccion, name="formulario_seccion"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/",buscar)
    ]
=======
    path ("formulario_articulo/", procesar_formulario_articulo, name="formulario_articulo")
    ]   
>>>>>>> 0d4f3f5489f92a7c36a52595a1679bdb12d832c3
