from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def probandoTemplate(self):
    
    nom = "Nicolas"
    ap = "Perez"
    
    listaDeNotas = [2,2,3,7,2,5]
    
    diccionario = {"nombre":nom, "apellido":ap, "notas":listaDeNotas}
    
    # miHtml = open("/home/finnegans/Escritorio/Emiliano/PROYECTO1/Proy_Uno/Proy_Uno/plantillas/template1.html")
    
    # plantilla = Template(miHtml.read())
    
    # miHtml.close()
    
    # miContexto = Context(diccionario)
    
    # documento = plantilla.render(miContexto)    

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)



