from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *


# Create your views here.
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

def buscarCampera(request):
    return render(request, "inicio/buscarCampera.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        talle = Campera.objects.filter(talle__icontains=patron)
        if talle:
            contexto = {'resultado':talle}
        elif talle:
            contexto = {'resultado':talle}
        color1 = Campera.objects.filter(color1__icontains=patron)
        if color1:
            contexto = {'resultado':color1}
        elif color1:
            contexto = {'resultado':color1}
        color2 = Campera.objects.filter(color2__icontains=patron)
        if color2:
            contexto = {'resultado':color2}
        elif color2:
            contexto = {'resultado':color2}
        modelo = Campera.objects.filter(modelo__icontains=patron)
        if modelo:
            contexto = {'resultado':modelo}
        elif modelo:
            contexto = {'resultado':modelo}
                                         
        return render(request, "inicio/campera.html", contexto)
    return HttpResponse("No se ingresó nada en buscar")


def buscarChaleco(request):
    return render(request, "inicio/buscarChaleco.html")

def buscar3(request):
    patron = request.GET.get('buscar')  # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_chaleco = Chaleco.objects.filter(talle__icontains=patron)
        color1_chaleco = Chaleco.objects.filter(color1__icontains=patron)
        color2_chaleco = Chaleco.objects.filter(color2__icontains=patron)
        modelo_chaleco = Chaleco.objects.filter(modelo__icontains=patron)

        buscar = talle_chaleco | color1_chaleco | color2_chaleco | modelo_chaleco

        if chaleco:
            contexto = {'chaleco': chaleco}
        else:
            contexto = {'mensaje': "No se encontraron chalecos"}

        return render(request, "inicio/chaleco.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

        
    