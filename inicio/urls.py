from django.urls import path, include
from .views import *
from .forms import *


urlpatterns = [
    path('', home, name="home" ),
    path('inicio/', inicio, name="inicio" ), 
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
]