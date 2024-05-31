from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    OPCIONES_ROL = (
        ('alumno', 'Alumno'),
        ('especialista', 'Especialista'),
    )
    rol = models.CharField(max_length=20, choices=OPCIONES_ROL)

class Alumno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    carrera = models.CharField(max_length=100)
    año = models.IntegerField()

class Especialista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50)

class PruebaEvaluacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_por = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    creado_el = models.DateTimeField(auto_now_add=True)

class Pregunta(models.Model):
    TIPOS_PREGUNTA = (
        ('opcion_multiple', 'Opción Múltiple'),
        ('verdadero_falso', 'Verdadero/Falso'),
        ('respuesta_abierta', 'Respuesta Abierta'),
    )
    prueba = models.ForeignKey(PruebaEvaluacion, on_delete=models.CASCADE)
    texto = models.TextField()
    tipo_pregunta = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)
    dificultad = models.IntegerField()

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.TextField()
    es_correcta = models.BooleanField()

class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, null=True, blank=True, on_delete=models.SET_NULL)
    texto_respuesta = models.TextField(null=True, blank=True)
    respondido_el = models.DateTimeField(auto_now_add=True)

class ResultadoEvaluacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebaEvaluacion, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentarios = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

class Tratamiento(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    plan_tratamiento = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Cita(models.Model):
    TIPOS_CITA = (
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
    )
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    tipo_cita = models.CharField(max_length=20, choices=TIPOS_CITA)
    notas = models.TextField()

class PruebaAnsiedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_por = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    creado_el = models.DateTimeField(auto_now_add=True)

class RespuestaPruebaAnsiedad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebaAnsiedad, on_delete=models.CASCADE)
    respuesta_1 = models.IntegerField()
    respuesta_2 = models.IntegerField()
    respuesta_3 = models.IntegerField()
    respuesta_4 = models.IntegerField()
    respuesta_5 = models.IntegerField()
    respuesta_6 = models.IntegerField()
    respuesta_7 = models.IntegerField()
    respuesta_8 = models.IntegerField()
    respuesta_9 = models.IntegerField()
    respuesta_10 = models.IntegerField()
    creado_el = models.DateTimeField(auto_now_add=True)

class ResultadoPruebaAnsiedad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebaAnsiedad, on_delete=models.CASCADE)
    puntuacion_total = models.IntegerField()
    interpretacion = models.TextField()
    recomendaciones = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)
