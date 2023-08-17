from django.urls import path, include
from .views import *
from .forms import *


urlpatterns = [
    path('', inicio, name="inicio" ), 
    path('campera/', campera, name="campera" ), 
    path('chaleco/', chaleco, name="chaleco" ), 
    path('pantalon/', pantalon, name="pantalon" ), 
    path('chaparreras/', chaparreras, name="chaparreras" ),
    path('guantes/', guantes, name="guantes" ),  
    
    path('campera_form/', camperaForm, name="campera_form" ),
    path('chaleco_form/', chalecoForm, name="chaleco_form" ),
    path('pantalon_form/', pantalonForm, name="pantalon_form" ),
    path('chaparreras_form/', chaparrerasForm, name="chaparreras_form" ),
    path('guantes_form/', guantesForm, name="guantes_form" ),
    
    path('buscar_campera/', buscarCampera, name="buscar_campera" ),
    path('buscar2/', buscar2, name="buscar2" ),
    
    path('buscar_chaleco/', buscarChaleco, name="buscar_chaleco" ),
    path('buscar3/', buscar3, name="buscar3" ),
    
    path('buscar_chaparreras/', buscarChaparreras, name="buscar_chaparreras" ),
    path('buscar4/', buscar4, name="buscar4" ),
    
    path('buscar_guantes/', buscarGuantes, name="buscar_guantes" ),
    path('buscar5/', buscar5, name="buscar5" ),
    
    path('buscar_pantalon/', buscarPantalon, name="buscar_pantalon" ),
    path('buscar6/', buscar6, name="buscar6" ),
]