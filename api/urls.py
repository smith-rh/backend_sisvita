from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'especialistas', views.EspecialistaViewSet)
router.register(r'pruebas-evaluacion', views.PruebaEvaluacionViewSet)
router.register(r'preguntas', views.PreguntaViewSet)
router.register(r'respuestas', views.RespuestaViewSet)
router.register(r'respuestas-usuario', views.RespuestaUsuarioViewSet)
router.register(r'resultados-evaluacion', views.ResultadoEvaluacionViewSet)
router.register(r'tratamientos', views.TratamientoViewSet)
router.register(r'citas', views.CitaViewSet)
router.register(r'pruebas-ansiedad', views.PruebaAnsiedadViewSet)
router.register(r'respuestas-prueba-ansiedad', views.RespuestaPruebaAnsiedadViewSet)
router.register(r'resultados-prueba-ansiedad', views.ResultadoPruebaAnsiedadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]