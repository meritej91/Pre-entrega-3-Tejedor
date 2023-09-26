from django import forms

class Mascota(forms.Form):

    nombre = forms.CharField()
    especie = forms.CharField()
    edad = forms.IntegerField()
    vacunas = forms.CharField()

class Empleado(forms.Form):
    apellido = forms.CharField()
    nombre = forms.CharField()
    dni = forms.IntegerField()

class Medicacion(forms.Form):
    nombre = forms.CharField()
    fecha_vencimiento = forms.DateField()