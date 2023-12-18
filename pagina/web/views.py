from django.shortcuts import render
from web.models import Aro, Cinturon, Malla
from django.http import HttpResponse

#Para CRUD
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy 

#Para el login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def pagina_principal(request):
    return render(request, 'index.html')

@login_required(login_url='Login') #si no estas logeado te dirije a esta seccion
def agregar_aro(request):
    if request.method == "POST":
        nuevo_aro = Aro(
            cod_producto_aro = (request.POST['cod_producto_aro']),
            material = (request.POST['material']),
            color = (request.POST['color']),
            precio = (request.POST['precio']),
            )
        nuevo_aro.save()
        return render(request, 'index.html')
    
    return render(request, 'agregar_aro.html')

@login_required(login_url='Login')
def agregar_cinto(request):
    if request.method == "POST":
        nuevo_cinto = Cinturon (
            cod_producto_cinto = (request.POST['cod_producto_cinto']),
            largo = (request.POST['largo']),
            color = (request.POST['color']),
            precio = (request.POST['precio']),
            )
        nuevo_cinto.save()
        return render(request, 'index.html')

    return render(request, 'agregar_cinto.html')

@login_required(login_url='Login')
def agregar_malla(request):
    if request.method == "POST":
        nuevo_malla = Malla (
            cod_producto_malla = (request.POST['cod_producto_malla']),
            modelo = (request.POST['modelo']),
            color = (request.POST['color']),
            talle = (request.POST['talle']),            
            precio = (request.POST['precio']),
            )
        nuevo_malla.save()
        return render(request, 'index.html')

    return render(request, 'agregar_malla.html')


####### Busqueda en base de datos #######

def buscar(request):
    return render(request, 'busqueda_talle.html')

def buscar_malla(request):
    if request.method == 'POST':
        talle = request.POST['talle']
        mallas_encontradas = Malla.objects.filter(talle=talle)
        #va a la base de datos, busca de todas las mallas, y las guarda en una lista nueva
        return render(request, 'resultados_busc.html', {'mallas_encontradas': mallas_encontradas})
    return render(request,'resultados_busc.html')


####### CRUD Aros #######
#creamos vistas con clases

class AroListView(ListView):
    model = Aro
    context_object_name = 'ListaAros'
    template_name = 'crud_aros/aro_lista.html'

class AroDetailView(DetailView):
    model = Aro
    template_name = 'crud_aros/aro_detalle.html'

@method_decorator(login_required(login_url='Login'), name='dispatch') #si no estas logeado te dirije a esta seccion
class AroUpdateView(UpdateView):
    model = Aro
    template_name = 'crud_aros/aro_editar.html'
    success_url = reverse_lazy('ListaAros') #nos redirige aca
    #recibe una cadena de string con el nombre de la vista al cual nos va a dirigir
    fields = ['cod_producto_aro','material','color','precio']
    #lista con los campos que queremos que se rendericen en nuestro formulario

@method_decorator(login_required(login_url='Login'), name='dispatch')
class AroDeleteView(DeleteView):
    model = Aro
    template_name = 'crud_aros/aro_borrar.html'
    success_url = reverse_lazy('ListaAros')


####### CRUD Cintos #######

class CintoListView(ListView):
    model = Cinturon
    context_object_name = 'ListaCintos'
    template_name = 'crud_cintos/cinto_lista.html'

class CintoDetailView(DetailView):
    model = Cinturon
    template_name = 'crud_cintos/cinto_detalle.html'

@method_decorator(login_required(login_url='Login'), name='dispatch')
class CintoUpdateView(UpdateView):
    model = Cinturon
    template_name = 'crud_cintos/cinto_editar.html'
    success_url = reverse_lazy('ListaCintos')
    fields = ['cod_producto_cinto','largo','color','precio']

@method_decorator(login_required(login_url='Login'), name='dispatch')
class CintoDeleteView(DeleteView):
    model = Cinturon
    template_name = 'crud_cintos/cinto_borrar.html'
    success_url = reverse_lazy('ListaCintos')


####### CRUD Mallas #######

class MallaListView(ListView):
    model = Malla
    context_object_name = 'ListaMallas'
    template_name = 'crud_mallas/malla_lista.html'

class MallaDetailView(DetailView):
    model = Malla
    template_name = 'crud_mallas/malla_detalle.html'

@method_decorator(login_required(login_url='Login'), name='dispatch')
class MallaUpdateView(UpdateView):
    model = Malla
    template_name = 'crud_mallas/malla_editar.html'
    success_url = reverse_lazy('ListaMallas')
    fields = ['cod_producto_malla','modelo','color','talle','precio']

@method_decorator(login_required(login_url='Login'), name='dispatch')
class MallaDeleteView(DeleteView):
    model = Malla
    template_name = 'crud_mallas/malla_borrar.html'
    success_url = reverse_lazy('ListaMallas')