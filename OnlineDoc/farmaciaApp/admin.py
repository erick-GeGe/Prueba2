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
