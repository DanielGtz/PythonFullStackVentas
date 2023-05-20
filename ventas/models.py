from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now=True)
    archivos = models.FileField(upload_to='archivos/', max_length=300, default='archivos/terminos_y_Condiciones_registro.pdf')
    activo = models.BooleanField(default=True)

    
    def __str__(self):
        return str(self.nombre)


class Personas(models.Model):
    ESTADOS = [ ('Chihuahua','Chihuahua'), ("Jalisco","Jalisco"), ("Michoacan","Michoacan")]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(max_length=100, choices=ESTADOS)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)


