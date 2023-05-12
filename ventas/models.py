from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now=True)
    archivo = models.FileField("PDF de prueba", upload_to='archivos/', max_length=300, default='archivos/terminos_y_Condiciones_registro.pdf')
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)

