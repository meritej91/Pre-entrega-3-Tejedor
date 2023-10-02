from django import forms

class MascotaForm(forms.Form):
    nombre = forms.CharField()
    especie = forms.CharField()
    edad = forms.IntegerField()
    vacunas = forms.CharField()

class EmpleadoForm(forms.Form):
    apellido = forms.CharField()
    nombre = forms.CharField()
    dni = forms.IntegerField()

class MedicacionForm(forms.Form):
    nombre = forms.CharField()
    fecha_vencimiento = forms.DateField()