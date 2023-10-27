from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    nombre = models.CharField(max_length=40)
    escudo = models.CharField (max_length=40)
    
class Jugador(models.Model):
    
    nombre = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    equipo = models.CharField(max_length=40)
    
class Partido(models.Model):
    
    fecha = models.IntegerField()
    equipo_Local = models.CharField(max_length=40)
    equipo_visitante = models.CharField(max_length=40)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()

