from django.shortcuts import render

# Create your views here.

from .models import Alumno

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/lista_alumnos.html', {'alumnos': alumnos})

