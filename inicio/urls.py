from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('inicio/', inicio, name="inicio" ), 
    path('campera/', campera, name="campera" ), 
    path('chaleco/', chaleco, name="chaleco" ), 
    path('pantalon/', pantalon, name="pantalon" ), 
    path('chaparreras/', chaparreras, name="chaparreras" ),
    path('guantes/', guantes, name="guantes" ),    
]