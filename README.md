# OnlineDoc Web

Pagina que ayuda a estar al danto de tu salud para que puedas vivir de manera feliz xd

## Comenzando 🚀

Para iniciar puedes descargar el proyecto y ubicarlo en una carpeta de tu preferencia, solo necesitas descomprimirlo, nada mas.     

### Pre-requisitos 📋

Tecnologia usadas en el proyecto

```
Python3
Pip
Django
Postgres
```

## Construido con 🛠️

* [django](https://www.djangoproject.com/) - El framework web usado
* [postgres](https://www.postgresql.org/) - Base de datos

## Proposito del proyecto
Es proposito fundamental de proyecto es poder poner al alcance de todos una aplicacion con la cual puedan estar al tanto de sus salud y de su bienestar personal


## Practicas codigo legible
```
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Cargar carpeta con django -->
    {% load static %}

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'onlineDocApp/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'onlineDocApp/css/style.css' %}">
</head>

<body>
    <!-- INCIO  -->
    <div class="text-center titulo">
        <h1 class="container ">OnlineDoc</h1>
    </div>
    <div class="container-fluid navbar-inverse bg-inverse  aumentada">
        <nav class="navbar navbar-toggleable-md container">
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
                data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <a class="navbar-brand " href="#">ProyectoWeb</a>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item {% if request.path == '/' %}active{% endif %}">
                        <a class="nav-link" href="/">Inicio </a>
                    </li>
                    <li class="nav-item {% if request.path == '/emergencia_medica' %}active{% endif %}">
                        <a class="nav-link" href="emergencia_medica">Emergencia medica</a>
                    </li>
                    <li class="nav-item {% if request.path == '/recibir_atencion_medica' %}active{% endif %}">
                        <a class="nav-link" href="recibir_atencion_medica">Recibir atencion medica</a>
                    </li>
                    <li class="nav-item {% if request.path == '/recibir_receta' %}active{% endif %}">
                        <a class="nav-link" href="recibir_receta">Recibir receta</a>
                    </li>
                    <li class="nav-item {% if request.path == '/reservar_cita' %}active{% endif %}">
                        <a class="nav-link" href="reservar_cita">Reservar cita</a>
                    </li>
                    <li class="nav-item {% if request.path == '/solicitar_atencion_fisica' %}active{% endif %}">
                        <a class="nav-link" href="solicitar_atencion_fisica">Solicitar atencion fisica</a>
                    </li>
                </ul>

            </div>
        </nav>
    </div>
    
    <!-- Contenido propio de cada pagina -->
    <div class="fondo-dark py-5 my-0">

        {% block content %}
        
        {% endblock %}
    </div>
 
    
    <!-- FOOTER -->
    <div class="final my-0">
        <footer class="footer text-xs-center container">
            <p>OnlineDoc Proyecto de Ingenieria de Software</p>
            <p>Numero para contratos 987654321</p>
        </footer>
    </div>


    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"
        integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"
        integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb"
        crossorigin="anonymous"></script>
    <script src="{% static 'onlineDocAppjs/bootstrap.min.js' %}"></script>
</body>

</html>

```

## Estilos de programacion ⌨️

Los estilos de programacion usados son los siguientes:

### 1. Things
Division del problema en partes mas pequeñas:
Urls

```
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

```
Views
```
from django.shortcuts import render, HttpResponse

def home(reques):
    return render(reques,"home.html")

def emergencia_medica(reques):
    return render(reques,"emergencia_medica.html")
```
Admin
```
from django.contrib import admin
from farmaciaApp import models

admin.site.register(models.Persona)
admin.site.register(models.Doctor)
admin.site.register(models.Usuario)
```

Models, etc ....


### 2. Trinity

#### Modelo 
Almacenamiento de datos
```
# Fragmento de archivo models

from django.db import models

class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, null=False)
    nombre = models.CharField(max_length=20, null=False)
    apellido_paterno = models.CharField(max_length=20, null=False)
    apellido_materno = models.CharField(max_length=20, null=False)
    celular = models.CharField(max_length=9, null=False)
```

#### Controlador
Control de los datos

```
from farmaciaApp.models import Personsa

personas = Persona.objects.all()
```

#### Vista Template
La vista decide que informacion vamos a mostrar y en que template

```
#Archivo views

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


```



### 3. Persistent Tables
Por el almacenamiento de los datos

```
class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, null=False)
    nombre = models.CharField(max_length=20, null=False)
    apellido_paterno = models.CharField(max_length=20, null=False)
    apellido_materno = models.CharField(max_length=20, null=False)
    celular = models.CharField(max_length=9, null=False)

class Doctor(models.Model):
    codigo_doctor = models.CharField(max_length=8, primary_key=True, null=False)
    dni_doctor = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False)
    especialidad = models.CharField(max_length=20, null=False)
    salario = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    horario_entrada = models.TimeField( null=False)
    horario_salida = models.TimeField( null=False)
```

## Principios SOLID

### S — Single Responsibility
Admin se encarga de las responsabilidades del administrador
```
from django.contrib import admin
from farmaciaApp import models

admin.site.register(models.Persona)
```

Views se encarga unicamente de las vistas
```
from django.shortcuts import render, HttpResponse

def home(reques):
    return render(reques,"home.html")
```

etc, etc
### O — Open-Closed
La clase models.Model puede ser extendida agregando nuevas funciones pero no puede ser modificada
```
from django.db import models

class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, null=False)
    nombre = models.CharField(max_length=20, null=False)
    apellido_paterno = models.CharField(max_length=20, null=False)
    apellido_materno = models.CharField(max_length=20, null=False)
    celular = models.CharField(max_length=9, null=False)
```
### D — Dependency Inversion
A la clase admin se le puede agregar cualquier clase de modelo para poder gestionarlo desde el administrador
```
from django.contrib import admin
from farmaciaApp import models

admin.site.register(models.Persona)
admin.site.register(models.Doctor)
admin.site.register(models.Usuario)
admin.site.register(models.Trabajador)
admin.site.register(models.Sala_virtual)
admin.site.register(models.Historia)
admin.site.register(models.Cita)
admin.site.register(models.Medicamento)
admin.site.register(models.Receta)
admin.site.register(models.Linea_receta)
```

