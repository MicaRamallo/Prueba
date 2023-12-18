from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta: #herramienta de django, una clase dentro de otra para definir algunos detalles extras
        model = User
        fields = ['username','email','password1','password2'] #campos de formulario
        #para sacar mensajes de ayuda
        help_texts = {k: '' for k in fields} #crear un diccionario por comprension

