from django import forms

class CamperaForm(forms.Form):
    talle = forms.CharField(max_length=50, required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class ChalecoForm(forms.Form):
    talle = forms.CharField(max_length=50, required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class ChaparrerasForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class GuantesForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    
class PantalonForm(forms.Form):
    talle = forms.IntegerField(required=True)
    color1= forms.CharField(max_length=50, required=True)
    color2 = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)            
    