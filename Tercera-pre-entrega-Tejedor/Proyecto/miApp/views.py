from django.shortcuts import render
from miApp.models import Mascota
from miApp.models import Empleado
from miApp.models import Medicacion
from miApp.forms import MascotaForm
from miApp.forms import EmpleadoForm
from miApp.forms import MedicacionForm
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

def formulario(request):
    if request.method == "POST":
        formulario1 = MascotaForm(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data

            nombre = MascotaForm(nombre=info["nombre"], especie=info["especie"], edad=info["edad"], vacunas=info["vacunas"])

            nombre.save()

            return render(request, "miApp/inicio.html")
    
    else:
        formulario1 = MascotaForm()

    return render(request, "miApp/formularios.html", {"form1":formulario1})

def busquedaMascota(request):

    return render(request, "miApp/busquedaMascota.html")

def resultado(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombre = Mascota.objects.filter(nombre_icontains=nombre)
        return HttpResponse(f"Estás buscando a la mascota:{request.GET['nombre']}")
    
    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


