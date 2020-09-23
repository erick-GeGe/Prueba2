from django.shortcuts import render, HttpResponse

def home(reques):
    return render(reques,"home.html")

def emergencia_medica(reques):
    return render(reques,"emergencia_medica.html")

def reservar_cita(reques):
    return render(reques,"reservar_cita.html")

def recibir_atencion_medica(reques):
    return render(reques,"recibir_atencion_medica.html")

def recibir_receta(reques):
    return render(reques,"recibir_receta.html")

def solicitar_atencion_fisica(reques):
    return render(reques,"solicitar_atencion_fisica.html")

