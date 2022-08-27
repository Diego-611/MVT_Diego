from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from django.template import loader

def mama (request):
    mama=Familia("Cristina","Gonzales",47,"11/04/1975","Trabaja en una obra social")
    adjunto_M="\nMi mama se llama ",mama.nombre,"\nSu apellido es ",mama.apellido,"\nElla tiene ",mama.edad," años","\nNacio el ",mama.cumpleaños,"\nEmpleo: ",mama.profesion
    descripcion_M={"descrip":adjunto_M}
    plantilla_M=loader.get_template ("Mama.html")
    documento_M=plantilla_M.render(descripcion_M)
    return HttpResponse (documento_M)

def papa (request):
    papa=Familia("Julio","Perez",58,"12/06/1964","Ingenieria en electronica")
    adjunto_P= "Mi papa se llama ",papa.nombre,"\nSu apellido es ",papa.apellido,"\nEl tiene ",papa.edad," años","\nNacio el ",papa.cumpleaños,"\nEmpleo: ",papa.profesion
    descripcion_P={"descrip":adjunto_P}
    plantilla_P=loader.get_template ("Papa.html")
    documento_P=plantilla_P.render(descripcion_P)
    return HttpResponse (documento_P)

def hermana (request):
    hermana=Familia("Pilar","Perez",16,"16/06/2006","Es estudiante de secundaria")
    adjunto_H= "Mi hermana se llama ",hermana.nombre,"\nSu apellido es ",hermana.apellido,"\nElla tiene ",hermana.edad," años","\nNacio el ",hermana.cumpleaños,"\nEmpleo: ",hermana.profesion
    descripcion_H={"descrip":adjunto_H}
    plantilla_H=loader.get_template ("Hermana.html")
    documento_H=plantilla_H.render(descripcion_H)
    return HttpResponse (documento_H)

def novia (request):
    novia=Familia("Gabriele","Ferrer",26,"06/08/1996","Trabaja en la joyeria de su PAPI")
    adjunto_N= "Mi novia se llama ",novia.nombre,"\nSu apellido es ",novia.apellido,"\nElla tiene ",novia.edad," años","\nNacio el ",novia.cumpleaños,"\nEmpleo: ",novia.profesion
    descripcion_N={"descrip":adjunto_N}
    plantilla_N=loader.get_template ("Novia.html")
    documento_N=plantilla_N.render(descripcion_N)
    return HttpResponse (documento_N)





