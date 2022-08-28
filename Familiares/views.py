from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from django.template import loader
from datetime import datetime

def mama (request):
    mama=Familia(nombre="Cristina",apellido="Gonzales",edad=47,nacimiento="11 de Mayo de 1975",profesion="Trabaja en una Obra Social")
    nom=mama.nombre
    ape=mama.apellido
    edad=mama.edad
    naci=mama.nacimiento
    prof=mama.profesion
    descripcion={"nom":nom, "ape":ape, "edad":edad,"naci":naci,"prof":prof}
    plantilla=loader.get_template ("Mama.html")
    documento=plantilla.render(descripcion)
    return HttpResponse (documento)

def papa (request):
    papa=Familia(nombre="Julio",apellido="Perez",edad=58,nacimiento="12 de Junio de 1964",profesion="Agricultura")
    nom=papa.nombre
    ape=papa.apellido
    edad=papa.edad
    naci=papa.nacimiento
    prof=papa.profesion
    descripcion={"nom":nom, "ape":ape, "edad":edad,"naci":naci,"prof":prof}
    plantilla=loader.get_template ("Papa.html")
    documento=plantilla.render(descripcion)
    return HttpResponse (documento)

def hermana (request):
    hermana=Familia(nombre="Pilar",apellido="Perez",edad=16,nacimiento="16 de Junio de 2006",profesion="No Trabaja")
    nom=hermana.nombre
    ape=hermana.apellido
    edad=hermana.edad
    naci=hermana.nacimiento
    prof=hermana.profesion
    descripcion={"nom":nom, "ape":ape, "edad":edad,"naci":naci,"prof":prof}
    plantilla=loader.get_template ("Hermana.html")
    documento=plantilla.render(descripcion)
    return HttpResponse (documento)
def novia (request):
    novia=Familia(nombre="Gabriele",apellido="Ferrer",edad=26,nacimiento="6 de Agosto de 1996",profesion="Trabaja en la joyeria de su PAPI")
    nom=novia.nombre
    ape=novia.apellido
    edad=novia.edad
    naci=novia.nacimiento
    prof=novia.profesion
    descripcion={"nom":nom, "ape":ape, "edad":edad,"naci":naci,"prof":prof}
    plantilla=loader.get_template ("Novia.html")
    documento=plantilla.render(descripcion)
    return HttpResponse (documento)





