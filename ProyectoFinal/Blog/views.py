from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mostrar_inicio(request):    
    return render(request,"Blog/inicio.html")