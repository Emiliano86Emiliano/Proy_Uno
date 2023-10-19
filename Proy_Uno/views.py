from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def probandoTemplate(self):
    
    miHtml = open("/home/finnegans/Escritorio/Emiliano/PROYECTO1/Proy_Uno/plantillas/template1.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)



