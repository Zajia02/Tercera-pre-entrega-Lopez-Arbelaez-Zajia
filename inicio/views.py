from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *


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

def camperaForm(request):
    if request.method == "POST":
        miForm = CamperaForm(request.POST)
        if miForm.is_valid():
            campera_talle = miForm.cleaned_data.get('talle')
            campera_color1 = miForm.cleaned_data.get('color1')
            campera_color2 = miForm.cleaned_data.get('color2')
            campera_modelo = miForm.cleaned_data.get('modelo')
            campera = Campera(talle=campera_talle,
                              color1=campera_color1,
                              color2=campera_color2,
                              modelo=campera_modelo)
            campera.save()
            return render(request, "inicio/base.html")
    else:
        miForm = CamperaForm()
        
    return render(request, "inicio/camperaForm.html", {"form": miForm})

def chalecoForm(request):
    if request.method == "POST":
        miForm = ChalecoForm(request.POST)
        if miForm.is_valid():
            chaleco_talle = miForm.cleaned_data.get('talle')
            chaleco_color1 = miForm.cleaned_data.get('color1')
            chaleco_color2 = miForm.cleaned_data.get('color2')
            chaleco_modelo = miForm.cleaned_data.get('modelo')
            chaleco = Chaleco(talle=chaleco_talle,
                              color1=chaleco_color1,
                              color2=chaleco_color2,
                              modelo=chaleco_modelo)
            chaleco.save()
            return render(request, "inicio/base.html")
    else:
        miForm = ChalecoForm()
        
    return render(request, "inicio/chalecoForm.html", {"form": miForm})

def chaparrerasForm(request):
    if request.method == "POST":
        miForm = ChaparrerasForm(request.POST)
        if miForm.is_valid():
            chaparreras_talle = miForm.cleaned_data.get('talle')
            chaparreras_color1 = miForm.cleaned_data.get('color1')
            chaparreras_color2 = miForm.cleaned_data.get('color2')
            chaparreras_modelo = miForm.cleaned_data.get('modelo')
            chaparreras = Chaparreras(talle=chaparreras_talle,
                              color1=chaparreras_color1,
                              color2=chaparreras_color2,
                              modelo=chaparreras_modelo)
            chaparreras.save()
            return render(request, "inicio/base.html")
    else:
        miForm = ChaparrerasForm()
        
    return render(request, "inicio/chaparrerasForm.html", {"form": miForm})

def guantesForm(request):
    if request.method == "POST":
        miForm = GuantesForm(request.POST)
        if miForm.is_valid():
            guantes_talle = miForm.cleaned_data.get('talle')
            guantes_color1 = miForm.cleaned_data.get('color1')
            guantes_color2 = miForm.cleaned_data.get('color2')
            guantes_modelo = miForm.cleaned_data.get('modelo')
            guantes = Guantes(talle=guantes_talle,
                              color1=guantes_color1,
                              color2=guantes_color2,
                              modelo=guantes_modelo)
            guantes.save()
            return render(request, "inicio/base.html")
    else:
        miForm = GuantesForm()
        
    return render(request, "inicio/guantesForm.html", {"form": miForm})

def pantalonForm(request):
    if request.method == "POST":
        miForm = PantalonForm(request.POST)
        if miForm.is_valid():
            pantalon_talle = miForm.cleaned_data.get('talle')
            pantalon_color1 = miForm.cleaned_data.get('color1')
            pantalon_color2 = miForm.cleaned_data.get('color2')
            pantalon_modelo = miForm.cleaned_data.get('modelo')
            pantalon = Pantalon(talle=pantalon_talle,
                              color1=pantalon_color1,
                              color2=pantalon_color2,
                              modelo=pantalon_modelo)
            pantalon.save()
            return render(request, "inicio/base.html")
    else:
        miForm = PantalonForm()
        
    return render(request, "inicio/pantalonForm.html", {"form": miForm})
    