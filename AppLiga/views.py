from django.shortcuts import render
from django.http import HttpResponse
from AppLiga.models import Equipo

# Create your views here.

def equipo(self):
    
    equipo = Equipo(nombre="San Sebastian",escudo="perro")
    equipo.save()
    documentoDeTexto = f"--> Equipo: {equipo.nombre} // Escudo: {equipo.escudo}"
    
    return HttpResponse(documentoDeTexto)


