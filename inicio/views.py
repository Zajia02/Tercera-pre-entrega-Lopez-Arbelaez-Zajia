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

# Formularios de agregación

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
            return HttpResponse("Se agregó la campera con éxito")
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
            return HttpResponse("Se agregó el chaleco con éxito")
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
            return HttpResponse("Se agregaron las chaparreras con éxito")
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
            return HttpResponse("Se agregaron los guantes con éxito")
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
            return HttpResponse("Se agregó el pantalón con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = PantalonForm()
        
    return render(request, "inicio/pantalonForm.html", {"form": miForm})
    

# Formularios de Búsqueda

def buscarCampera(request):
    return render(request, "inicio/buscarCampera.html")

def buscar2(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_campera = Campera.objects.filter(talle__icontains=patron)
        color1_campera = Campera.objects.filter(color1__icontains=patron)
        color2_campera = Campera.objects.filter(color2__icontains=patron)
        modelo_campera = Campera.objects.filter(modelo__icontains=patron)

        if talle_campera:
            contexto = {'campera': talle_campera}
        elif color1_campera:
            contexto = {'campera': color1_campera}
        elif color2_campera:
            contexto = {'campera': color2_campera}
        elif modelo_campera:
            contexto = {'campera': modelo_campera}
        else:
            return HttpResponse("No se encontraron camperas")   

        return render(request, "inicio/campera.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

def buscarChaleco(request):
    return render(request, "inicio/buscarChaleco.html")

def buscar3(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_chaleco = Chaleco.objects.filter(talle__icontains=patron)
        color1_chaleco = Chaleco.objects.filter(color1__icontains=patron)
        color2_chaleco = Chaleco.objects.filter(color2__icontains=patron)
        modelo_chaleco = Chaleco.objects.filter(modelo__icontains=patron)

        if talle_chaleco:
            contexto = {'chaleco': talle_chaleco}
        elif color1_chaleco:
            contexto = {'chaleco': color1_chaleco}
        elif color2_chaleco:
            contexto = {'chaleco': color2_chaleco}
        elif modelo_chaleco:
            contexto = {'chaleco': modelo_chaleco}
        else:
            return HttpResponse("No se encontraron chalecos")    

        return render(request, "inicio/chaleco.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")
    
def buscarChaparreras(request):
    return render(request, "inicio/buscarChaparreras.html")

def buscar4(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_chaparreras = Chaparreras.objects.filter(talle__icontains=patron)
        color1_chaparreras = Chaparreras.objects.filter(color1__icontains=patron)
        color2_chaparreras = Chaparreras.objects.filter(color2__icontains=patron)
        modelo_chaparreras = Chaparreras.objects.filter(modelo__icontains=patron)

        if talle_chaparreras:
            contexto = {'chaparreras': talle_chaparreras}
        elif color1_chaparreras:
            contexto = {'chaparreras': color1_chaparreras}
        elif color2_chaparreras:
            contexto = {'chaparreras': color2_chaparreras}
        elif modelo_chaparreras:
            contexto = {'chaparreras': modelo_chaparreras}
        else:
            return HttpResponse("No se encontraron chaparreras")    

        return render(request, "inicio/chaparreras.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")
    
def buscarGuantes(request):
    return render(request, "inicio/buscarGuantes.html")

def buscar5(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_guantes = Guantes.objects.filter(talle__icontains=patron)
        color1_guantes = Guantes.objects.filter(color1__icontains=patron)
        color2_guantes = Guantes.objects.filter(color2__icontains=patron)
        modelo_guantes = Guantes.objects.filter(modelo__icontains=patron)

        if talle_guantes:
            contexto = {'guantes': talle_guantes}
        elif color1_guantes:
            contexto = {'guantes': color1_guantes}
        elif color2_guantes:
            contexto = {'guantes': color2_guantes}
        elif modelo_guantes:
            contexto = {'guantes': modelo_guantes}
        else:
            return HttpResponse("No se encontraron guantes")    

        return render(request, "inicio/guantes.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

def buscarPantalon(request):
    return render(request, "inicio/buscarPantalon.html")    
    
def buscar6(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_pantalon = Pantalon.objects.filter(talle__icontains=patron)
        color1_pantalon = Pantalon.objects.filter(color1__icontains=patron)
        color2_pantalon = Pantalon.objects.filter(color2__icontains=patron)
        modelo_pantalon = Pantalon.objects.filter(modelo__icontains=patron)

        if talle_pantalon:
            contexto = {'pantalon': talle_pantalon}
        elif color1_pantalon:
            contexto = {'pantalon': color1_pantalon}
        elif color2_pantalon:
            contexto = {'pantalon': color2_pantalon}
        elif modelo_pantalon:
            contexto = {'pantalon': modelo_pantalon}
        else:
            return HttpResponse("No se encontraron pantalones")    

        return render(request, "inicio/pantalon.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")        

        
    