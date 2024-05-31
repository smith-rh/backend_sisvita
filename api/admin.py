from django.contrib import admin
from .models import (
    Usuario, Alumno, Especialista, PruebaEvaluacion, Pregunta,
    Respuesta, RespuestaUsuario, ResultadoEvaluacion, Tratamiento, Cita, PruebaAnsiedad,
    RespuestaPruebaAnsiedad, ResultadoPruebaAnsiedad)

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('rol',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'matricula', 'carrera', 'año')
    search_fields = ('matricula', 'carrera', 'año')

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad', 'numero_licencia')
    search_fields = ('especialidad', 'numero_licencia')

@admin.register(PruebaEvaluacion)
class PruebaEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'creado_por', 'creado_el')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('creado_por', 'creado_el')

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'prueba', 'tipo_pregunta', 'dificultad')
    search_fields = ('texto',)
    list_filter = ('prueba', 'tipo_pregunta', 'dificultad')

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'pregunta', 'es_correcta')
    search_fields = ('texto',)
    list_filter = ('pregunta', 'es_correcta')

@admin.register(RespuestaUsuario)
class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pregunta', 'respuesta', 'texto_respuesta', 'respondido_el')
    search_fields = ('texto_respuesta',)
    list_filter = ('usuario', 'pregunta', 'respondido_el')

@admin.register(ResultadoEvaluacion)
class ResultadoEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'prueba', 'puntuacion', 'comentarios', 'creado_el')
    search_fields = ('comentarios',)
    list_filter = ('usuario', 'prueba', 'creado_el')

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'especialista', 'diagnostico', 'plan_tratamiento', 'fecha_inicio', 'fecha_fin')
    search_fields = ('diagnostico', 'plan_tratamiento')
    list_filter = ('alumno', 'especialista', 'fecha_inicio', 'fecha_fin')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'especialista', 'fecha_cita', 'tipo_cita', 'notas')
    search_fields = ('notas',)
    list_filter = ('alumno', 'especialista', 'fecha_cita', 'tipo_cita')

@admin.register(PruebaAnsiedad)
class PruebaAnsiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'creado_por', 'creado_el')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('creado_por', 'creado_el')

@admin.register(RespuestaPruebaAnsiedad)
class RespuestaPruebaAnsiedadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'prueba', 'respuesta_1', 'respuesta_2', 'respuesta_3', 'respuesta_4', 'respuesta_5', 'respuesta_6', 'respuesta_7', 'respuesta_8', 'respuesta_9', 'respuesta_10', 'creado_el')
    list_filter = ('usuario', 'prueba', 'creado_el')

@admin.register(ResultadoPruebaAnsiedad)
class ResultadoPruebaAnsiedadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'prueba', 'puntuacion_total', 'interpretacion', 'recomendaciones', 'creado_el')
    search_fields = ('interpretacion', 'recomendaciones')
    list_filter = ('usuario', 'prueba', 'creado_el')
