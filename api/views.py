from rest_framework import viewsets

from .models import (
    Usuario, Alumno, Especialista, PruebaEvaluacion, Pregunta, Respuesta,
    RespuestaUsuario, ResultadoEvaluacion, Tratamiento, Cita, PruebaAnsiedad,
    RespuestaPruebaAnsiedad, ResultadoPruebaAnsiedad
)
from .serializer import (
    UsuarioSerializer, AlumnoSerializer, EspecialistaSerializer,
    PruebaEvaluacionSerializer, PreguntaSerializer, RespuestaSerializer,
    RespuestaUsuarioSerializer, ResultadoEvaluacionSerializer, TratamientoSerializer,
    CitaSerializer, PruebaAnsiedadSerializer, RespuestaPruebaAnsiedadSerializer,
    ResultadoPruebaAnsiedadSerializer
)

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

class PruebaEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = PruebaEvaluacion.objects.all()
    serializer_class = PruebaEvaluacionSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

class RespuestaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaUsuario.objects.all()
    serializer_class = RespuestaUsuarioSerializer

class ResultadoEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = ResultadoEvaluacion.objects.all()
    serializer_class = ResultadoEvaluacionSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class PruebaAnsiedadViewSet(viewsets.ModelViewSet):
    queryset = PruebaAnsiedad.objects.all()
    serializer_class = PruebaAnsiedadSerializer

class RespuestaPruebaAnsiedadViewSet(viewsets.ModelViewSet):
    queryset = RespuestaPruebaAnsiedad.objects.all()
    serializer_class = RespuestaPruebaAnsiedadSerializer

class ResultadoPruebaAnsiedadViewSet(viewsets.ModelViewSet):
    queryset = ResultadoPruebaAnsiedad.objects.all()
    serializer_class = ResultadoPruebaAnsiedadSerializer
