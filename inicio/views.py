from django.shortcuts import render

from .models import *

# Create your views here.
def home(request):
    return render(request, "inicio/home.html")

def inicio(request):
    return render(request, "inicio/inicio.html")

def campera(request):
    contexto = {'campera': Campera.objects.all() }
    return render(request, "inicio/campera.html", contexto)

def chaleco(request):
    contexto = {'chaleco': Chaleco.objects.all() }
    return render(request, "inicio/chaleco.html", contexto)

def pantalon(request):
    contexto = {'pantalon': Pantalon.objects.all() }
    return render(request, "inicio/pantalon.html", contexto)

def chaparreras(request):
    contexto = {'chaparreras': Chaparreras.objects.all() }
    return render(request, "inicio/chaparreras.html", contexto)

def guantes(request):
    contexto = {'guantes': Guantes.objects.all() }
    return render(request, "inicio/guantes.html", contexto)


    