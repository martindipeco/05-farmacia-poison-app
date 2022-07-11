from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Listado
from .forms import ListadoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def horarios(request):
    return render(request, 'horarios.html')

def registro(request):
    return render(request, 'registro.html')

def chango(request):
    return render(request, 'chango.html')

def proximamente(request):
    return render(request, 'proximamente.html')

def listado(request):
    listado = Listado.objects.all
    return render(request, 'listado.html', {'listado': listado})

def crear(request):
    formulario = ListadoForm(request.POST or None, request.FILES or None)
    #Cuando el formulario se envía con datos
    if formulario.is_valid():
        formulario.save()
        return redirect('listado')
    return render(request, 'crear.html', {'formulario': formulario})

def eliminar(request, id):
    producto = Listado.objects.get(id=id)
    producto.delete()
    return redirect('listado')

def editar(request, id):
    producto = Listado.objects.get(id=id)
    formulario = ListadoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado')
    return render(request, 'editar.html', {'formulario': formulario})

