from django import forms

class MallaFormulario (forms.Form):
    cod_producto_malla = forms.IntegerField()
    modelo = forms.CharField()
    color = forms.CharField()
    talle = forms.IntegerField()
    precio = forms.IntegerField()
