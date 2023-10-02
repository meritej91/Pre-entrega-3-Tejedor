from django.urls import path
from miApp.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("mascotas/", mascota, name="Mascota"),
    path("empleado/", empleado, name="Empleado"),
    path("medicacion/", medicacion, name="Medicación"),
    path("formularios/", formulario, name="Formulario"),
    path("busquedaMascota/", busquedaMascota, name="BuscarMascota"),
    path("resultados/", resultado, name="ResultadosBusqueda"),
]