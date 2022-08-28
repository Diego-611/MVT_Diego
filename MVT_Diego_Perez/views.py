from django.http import HttpResponse
from django.template import loader
from Familiares.views import *

def inicio (request):
    inicio={"Presentacion":"Bienvendio A Mi Familia"}
    plantilla_inicio=loader.get_template("Inicio.html")
    documento=plantilla_inicio.render(inicio)
    return HttpResponse (documento)



