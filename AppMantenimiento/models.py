from django.db import models

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año_fabricacion = models.PositiveIntegerField()
    patente = models.CharField(max_length=20)
    mecanico = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca} - {self.modelo} ({self.año_fabricacion}) atendido por {self.mecanico}"

class Mantenimiento(models.Model):
    vehiculo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Mantenimiento de {self.vehiculo} - {self.fecha}"
