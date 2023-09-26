from django.db import models

class Mascota(models.Model):

    nombre = models.CharField(max_length=15)
    especie = models.CharField(max_length=15)
    edad = models.IntegerField()
    vacunas = models.CharField(max_length=40)

class Empleado(models.Model):
    apellido = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()

class Medicacion(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()



    


