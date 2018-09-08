from django.urls import path, include
from apps.home.views import *

urlpatterns = [
    path('', inicio_view ,name='inicio' ),
    
    path('lugar_agregar/', lugar_agregar_view ,name='lugar_agregar' ),
    path('lugar_listar/', lugar_listar_view ,name='lugar_listar' ),
    path('lugar_ver/<int:pk>/', lugar_ver_view ,name='lugar_ver' ),
    path('lugar_editar/<int:pk>/', lugar_editar_view ,name='lugar_editar' ),
    path('lugar_eliminar/<int:pk>/', lugar_eliminar_view ,name='lugar_eliminar' ),

    
    path('galeria_agregar/', galeria_agregar_view ,name='galeria_agregar' ),
    path('galeria_listar/', galeria_listar_view ,name='galeria_listar' ),
    path('galeria_ver/<int:pk>/', galeria_ver_view ,name='galeria_ver' ),
    path('galeria_editar/<int:pk>/', galeria_editar_view ,name='galeria_editar' ),
    path('galeria_eliminar/<int:pk>/', galeria_eliminar_view ,name='galeria_eliminar' ),

    
    # path('tipo_sitio_agregar/', tipo_sitio_agregar_view ,name='tipo_sitio_agregar' ),
    # path('tipo_sitio_listar/', tipo_sitio_listar_view ,name='tipo_sitio_listar' ),
    # path('tipo_sitio_ver/<int:pk>/', tipo_sitio_ver_view ,name='tipo_sitio_ver' ),
    # path('tipo_sitio_editar/<int:pk>/', tipo_sitio_editar_view ,name='tipo_sitio_editar' ),
    # path('tipo_sitio_eliminar/<int:pk>/', tipo_sitio_eliminar_view ,name='tipo_sitio_eliminar' ),

    
    # path('sitio_agregar/', sitio_agregar_view ,name='sitio_agregar' ),
    # path('sitio_listar/', sitio_listar_view ,name='sitio_listar' ),
    # path('sitio_ver/<int:pk>/', sitio_ver_view ,name='sitio_ver' ),
    # path('sitio_editar/<int:pk>/', sitio_editar_view ,name='sitio_editar' ),
    # path('sitio_eliminar/<int:pk>/', sitio_eliminar_view ,name='sitio_eliminar' ),

    
    # path('tipo_restaurante_agregar/', tipo_restaurante_agregar_view ,name='tipo_restaurante_agregar' ),
    # path('tipo_restaurante_listar/', tipo_restaurante_listar_view ,name='tipo_restaurante_listar' ),
    # path('tipo_restaurante_ver/<int:pk>/', tipo_restaurante_ver_view ,name='tipo_restaurante_ver' ),
    # path('tipo_restaurante_editar/<int:pk>/', tipo_restaurante_editar_view ,name='tipo_restaurante_editar' ),
    # path('tipo_restaurante_eliminar/<int:pk>/', tipo_restaurante_eliminar_view ,name='tipo_restaurante_eliminar' ),

    
    # path('restaurante_agregar/', restaurante_agregar_view ,name='restaurante_agregar' ),
    # path('restaurante_listar/', restaurante_listar_view ,name='restaurante_listar' ),
    # path('restaurante_ver/<int:pk>/', restaurante_ver_view ,name='restaurante_ver' ),
    # path('restaurante_editar/<int:pk>/', restaurante_editar_view ,name='restaurante_editar' ),
    # path('restaurante_eliminar/<int:pk>/', restaurante_eliminar_view ,name='restaurante_eliminar' ),

    
    # path('hotel_agregar/', hotel_agregar_view ,name='hotel_agregar' ),
    # path('hotel_listar/', hotel_listar_view ,name='hotel_listar' ),
    # path('hotel_ver/<int:pk>/', hotel_ver_view ,name='hotel_ver' ),
    # path('hotel_editar/<int:pk>/', hotel_editar_view ,name='hotel_editar' ),
    # path('hotel_eliminar/<int:pk>/', hotel_eliminar_view ,name='hotel_eliminar' ),



]

'''
Lugar
Galeria
Tipo_Sitio
Sitio
Tipo_Restaurante
Restaurante
Hotel'''