from django.urls import path

from farmaciaApp import views

urlpatterns = [
    path('', views.home),
    path('emergencia_medica', views.emergencia_medica),
    path('recibir_atencion_medica', views.recibir_atencion_medica),
    path('recibir_receta', views.recibir_receta),
    path('reservar_cita', views.reservar_cita),
    path('solicitar_atencion_fisica', views.solicitar_atencion_fisica),
]