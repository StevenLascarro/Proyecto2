from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Importar Modelo
from .models import Campeon

# Create your views here.
def index(request):
    #Consultar listado de registros de base de datos
    lista_campeones = Campeon.objects.all()    
    template = loader.get_template("index.html")
    #Agregar pokemones al contexto del template
    context = {"campeones":lista_campeones}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id_campeon):
    #Consultar el registro en base de datos
    detalle_campeon = Campeon.objects.get(id = id_campeon)
    #Obtener template
    template = loader.get_template("detail.html")
    #Agregar los datos del registro al contexto del template
    context = {"campeon":detalle_campeon}
    return HttpResponse(template.render(context,request))    