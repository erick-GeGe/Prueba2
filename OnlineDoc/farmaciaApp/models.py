from django.db import models

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

class Trabajador(models.Model):
    codigo_trabajador  = models.CharField(max_length=8,primary_key=True, null=False)
    dni_trabajador = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False)
    cargo = models.CharField(max_length=20, null=False)
    salario = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    horario_entrada = models.TimeField(null=False)
    horario_salida = models.TimeField(null=False)

class Usuario(models.Model):
    codigo_usuario = models.CharField(max_length=8, primary_key=True, null=False)
    dni_usuario = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False)

class Sala_virtual(models.Model):
    codigo_sala = models.CharField(max_length=8, null=False)
    codigo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    codigo_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    especialidad = models.CharField(max_length=20, null=False)
    horario_inicio = models.TimeField(null=False)
    horario_final = models.TimeField(null=False)
    link_meet = models.CharField(max_length=50,null=False)

class Historia(models.Model):
    codigo_historia = models.CharField(max_length=8, null=False)
    codigo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)

class Cita(models.Model):
    codigo_cita = models.CharField(max_length=8, null=False)
    codigo_historia = models.ForeignKey(Historia, on_delete=models.CASCADE, null=False)
    codigo_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    fecha = models.TimeField( null=False)

class Medicamento(models.Model):
    codigo_medicamento = models.CharField(max_length=8, null=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    stock = models.IntegerField( null=False)
    indicaciones = models.CharField(max_length=50,  null=False)

class Receta(models.Model):
    codigo_receta = models.CharField(max_length=8,  null=False)
    observaciones = models.CharField(max_length=20,  null=False)
    codigo_sala = models.CharField(max_length=8,  null=False)
    codigo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,  null=False)
    codigo_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,  null=False)

class Linea_receta(models.Model):
    numero_linea = models.CharField(max_length=4,  null=False)
    codigo_receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False)
    codigo_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField( null=False)
    indicaciones = models.CharField(max_length=50,  null=False)