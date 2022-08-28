from django.db import models

class Familia (models.Model):
    nombre=models.CharField(max_length=12)
    apellido=models.CharField(max_length=16)
    edad=models.IntegerField()
    nacimiento=models.CharField(max_length=100)
    profesion=models.CharField(max_length=100)
