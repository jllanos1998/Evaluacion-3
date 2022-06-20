from django.db import models

# Create your models here.

class Jaime(models.Model):
    SEXO = (
        ('F', 'femenino'),
        ('M', 'masculino')
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)

   
