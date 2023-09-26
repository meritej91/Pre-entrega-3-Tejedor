from django.shortcuts import render
from miApp.models import Mascota
from miApp.models import Empleado
from miApp.models import Medicacion
from django.http import HttpResponse

def inicio(request):
    return render(request, "miApp/inicio.html")

def mascota(request):
   if request.method == "POST":
       
       mascota = Mascota(nombre=request.POST["Nombre"], especie=request.POST["Especie"], edad=request.POST["Edad"], vacunas=request.POST["Vacunas"])
       mascota.save()

       return render(request, "miApp/inicio.html")

def empleado(request):
    if request.method == "POST":
       
       empleado = Empleado(apellido=request.POST["Apellido"], nombre=request.POST["Nombre"], dni=request.POST["DNI"])
       empleado.save()


    return render(request, "miApp/inicio.html")

def medicacion(request):
    if request.method == "POST":
       
       medicacion = Medicacion(nombre=request.POST["Nombre"], fecha_vencimiento=request.POST["Fecha de vencimiento"])
       medicacion.save()
    return render(request, "miApp/inicio.html")