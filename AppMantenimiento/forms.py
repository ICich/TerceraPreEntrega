from django import forms

class MecanicoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    año_fabricacion = forms.IntegerField()
    patente = forms.CharField(max_length=20)
    mecanico = forms.CharField(max_length=100)

class MantenimientoForm(forms.Form):
    vehiculo = forms.CharField(max_length=100)
    fecha = forms.DateField()
    descripcion = forms.CharField()