from django.shortcuts import render, redirect
from .models import Taks
# Create your views here.
def index(request):
    taks = Taks.objects.all()
    return render(request, "taks/index.html", {"taks": taks [::-1],"update": None})

def create_taks(request):
    tak = Taks(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
    tak.save()
    return redirect('/taks/')

def update(request):
    tak_id = request.POST['id']
    tak_nombre = request.POST['nombre']
    tak_descripcion = request.POST['descripcion']
    task = Taks.objects.get(pk=tak_id)
    task.nombre = tak_nombre
    task.descripcion = tak_descripcion
    task.save()
    return redirect('/taks/')

def update_taks(request, taks_id):
    tak = Taks.objects.all()
    tak_only = Taks.objects.get(pk=taks_id)
    return render(request, "taks/index.html", {"taks": tak [::-1],"update": tak_only})

def delete_taks(request, taks_id):
    tak = Taks.objects.get(id=taks_id)
    tak.delete()
    return redirect('/taks/')
