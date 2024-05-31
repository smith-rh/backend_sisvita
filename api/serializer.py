from rest_framework import serializers
from .models import (
    Usuario, Alumno, Especialista, PruebaEvaluacion, Pregunta, Respuesta,
    RespuestaUsuario, ResultadoEvaluacion, Tratamiento, Cita, PruebaAnsiedad,
    RespuestaPruebaAnsiedad, ResultadoPruebaAnsiedad
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = '__all__'

class PruebaEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaEvaluacion
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'

class RespuestaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaUsuario
        fields = '__all__'

class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class PruebaAnsiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaAnsiedad
        fields = '__all__'

class RespuestaPruebaAnsiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPruebaAnsiedad
        fields = '__all__'

class ResultadoPruebaAnsiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoPruebaAnsiedad
        fields = '__all__'
