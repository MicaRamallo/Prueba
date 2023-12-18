from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from usuarios.forms import CustomUserCreationForm 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.views import LogoutView 
from django.views.generic import CreateView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from usuarios.models import PerfilUsuario
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

####### LOGIN Y LOGOUT #######

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST) #formulario hecho automaticamente
        if form.is_valid(): #si pasó la validacion de django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate (username=usuario, password=contrasenia) #verifica para hacer el login
            #si los datos son correctos, estamos entrando a la pagina con un usuario registrado
            login(request,user)
            return render(request, 'index.html', {'mensaje': f'Bienvenido {user.username}'}) #te manda al inicio
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form':form})

def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) #creamos el formulario
        if form.is_valid(): #validamos si es valido para django
            username = form.cleaned_data['username']
            form.save() #guardamos el usuario
            return render(request, 'index.html', {'mensaje':'Usuario ' + username + ' registrado'})
        else:
            return render(request, 'usuarios/registro.html',{'form':form})
    else:
        form = CustomUserCreationForm()
        return render (request, 'usuarios/registro.html', {'form':form})

class Logout(LogoutView):
    template_name = 'usuarios/logout.html'

class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "usuarios/crear_perfil.html"
    success_url = reverse_lazy ("VerPerfil")
    fields = ['usuario', 'imagen', 'rol']
    login_url = "/usuarios/login"

class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    template_name = "usuarios/editar_perfil.html"
    success_url = reverse_lazy ("VerPerfil")
    fields = ['imagen', 'rol']
    login_url = "/usuarios/login"

@login_required(login_url="Login") #solo lo veo si estoy logeado
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, "usuarios/perfil.html") 
    except:
        return redirect ("CrearPerfil")