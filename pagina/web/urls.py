from django.urls import path
from web import views

urlpatterns = [
    path('agregar_aro/', views.agregar_aro, name ='agregar aro'),
    path('agregar_cinto/', views.agregar_cinto, name ='agregar cinto'),
    path('agregar_malla/', views.agregar_malla, name ='agregar_malla'),
    #la otra forma de hacer formularios -> form
    #path('malla_formulario/',views.malla_formulario, name='agregar malla')
    path('busqueda_talle/', views.buscar_malla),
    path('buscar/', views.buscar),

    #Para CRUD
    path('crud_aros/aro_lista/', views.AroListView.as_view(), name = 'ListaAros'),
    path('crud_aros/<pk>/aro_detalle/', views.AroDetailView.as_view(), name = 'DetalleAro'),
    path('crud_aros/<pk>/aro_editar/', views.AroUpdateView.as_view(), name = 'EditarAro'),
    path('crud_aros/<pk>/aro_borrar/', views.AroDeleteView.as_view(), name = 'BorrarAro'),

    path('crud_cintos/cinto_lista/', views.CintoListView.as_view(), name = 'ListaCintos'),
    path('crud_cintos/<pk>/cinto_detalle/', views.CintoDetailView.as_view(), name = 'DetalleCinto'),
    path('crud_cintos/<pk>/cinto_editar/', views.CintoUpdateView.as_view(), name = 'EditarCinto'),
    path('crud_cintos/<pk>/cinto_borrar/', views.CintoDeleteView.as_view(), name = 'BorrarCinto'),

    path('crud_mallas/malla_lista/', views.MallaListView.as_view(), name = 'ListaMallas'),
    path('crud_mallas/<pk>/malla_detalle/', views.MallaDetailView.as_view(), name = 'DetalleMalla'),
    path('crud_mallas/<pk>/malla_editar/', views.MallaUpdateView.as_view(), name = 'EditarMalla'),
    path('crud_mallas/<pk>/malla_borrar/', views.MallaDeleteView.as_view(), name = 'BorrarMalla'),

]