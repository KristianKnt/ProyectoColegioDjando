from tkinter.messagebox import RETRY
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Estudiante
from .forms import EstudianteForm
# Create your views here.


def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def materias(request):
    estudiante = Estudiante.objects.all()
    return render(request,'materias/index.html',{'estudiante':estudiante})





def crear(request):
    formulario = EstudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('materias')
    return render(request, 'materias/crear.html',{'formulario':formulario})
    
def editar(request,id):
    estudiante = Estudiante.objects.get(id=id)
    formulario = EstudianteForm(request.POST or None, request.FILES or None, instance=estudiante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('materias')
    return render(request,'materias/editar.html',{'formulario':formulario})

def eliminar(request,id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('materias')


