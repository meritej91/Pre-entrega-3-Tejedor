from django.urls import path
from miApp.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("mascotas/", mascota, name="Mascota"),
    path("empleado/", empleado, name="Empleado"),
    path("medicacion/", medicacion, name="Medicación"),
]