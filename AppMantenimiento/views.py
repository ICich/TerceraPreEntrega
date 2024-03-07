from django.shortcuts import render
from .models import Mecanico, Vehiculo, Mantenimiento
from .forms import MecanicoForm, VehiculoForm, MantenimientoForm

# Create your views here.

def agregar_mecanico(request):
    
    if request.method == "POST":
        
        formulario = MecanicoForm(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_mecanico = Mecanico(nombre = info_dict["nombre"],
                                      apellido = info_dict["apellido"],
                                      especialidad = info_dict["especialidad"])
            
            nuevo_mecanico.save()
            
            return render(request, "AppMantenimiento/inicio.html")
    else:
        
        formulario = MecanicoForm()
                                                 
    return render(request, "AppMantenimiento/nuevo_mecanico.html", {"form":formulario})


def agregar_vehiculo(request):
    
    if request.method == "POST":
        
        formulario = VehiculoForm(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_vehiculo = Vehiculo(marca = info_dict["marca"],
                                      modelo = info_dict["modelo"],
                                      año_fabricacion = info_dict["año_fabricacion"],
                                      patente = info_dict["patente"],
                                      mecanico = info_dict["mecanico"])
            
            nuevo_vehiculo.save()
            
            return render(request, "AppMantenimiento/inicio.html")
    else:
        
        formulario = VehiculoForm()

    return render(request, "AppMantenimiento/nuevo_vehiculo.html", {"form":formulario})


def agregar_mantenimiento(request):
    
    if request.method == "POST":
        
        formulario = MantenimientoForm(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_mantenimiento = Mantenimiento(vehiculo = info_dict["vehiculo"],
                                      fecha = info_dict["fecha"],
                                      descripcion = info_dict["descripcion"])
            
            nuevo_mantenimiento.save()
            
            return render(request, "AppMantenimiento/inicio.html")
    else:
        
        formulario = MantenimientoForm()
    
    return render(request, "AppMantenimiento/nuevo_mantenimiento.html", {"form":formulario})


def buscar_mecanico(request):
    
    return render(request, "AppMantenimiento/buscar_mecanico.html")

def mostrar_mecanico(request):
    
    mecanico = request.GET["mecanico"]
    
    resultado = Mecanico.objects.filter(nombre=mecanico)
    
    return render(request, "AppMantenimiento/resultado.html", {"resultado":resultado})