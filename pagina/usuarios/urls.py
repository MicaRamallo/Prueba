from django.urls import path
from usuarios import views

urlpatterns = [
    #A partir de aca va en la nueva app usuarios
    #Login y logout
    path('login/', views.login_request, name = 'Login'),
    path('registro/', views.registro, name = 'Registro'),
    path('logout/', views.Logout.as_view(), name = 'Logout'),
    path('crear_perfil/', views.PerfilUsuarioCreateView.as_view(), name='CrearPerfil'),
    path('/<pk>/editar_perfil/', views.PerfilUsuarioUpdateView.as_view(), name='EditarPerfil'),
    path('perfil_usuario/', views.perfil_usuario, name='VerPerfil'),
]