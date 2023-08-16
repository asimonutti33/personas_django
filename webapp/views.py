from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    nro_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'Nro de personas': nro_personas, 'personas': personas} )

