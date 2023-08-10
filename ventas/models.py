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



class cat_Estado(models.Model):	
	entidad_federativa = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	default = models.IntegerField(default=0)
	orden = models.IntegerField(default=1)
	codigo = models.CharField(max_length=45, blank=True)
	estatus = models.BooleanField(default=True)
		
	def __str__(self):
		return str(self.entidad_federativa)

class cat_Municipio(models.Model):

		clave = models.CharField(max_length=100)
		valor = models.CharField(max_length=250)
		cat_entidades_federativas = models.ForeignKey(cat_Estado, on_delete=models.CASCADE, related_name='fk_Municipio_Estado',default=1)
		created_at = models.DateTimeField(auto_now=True)
		updated_at = models.DateTimeField(auto_now=True)
		estatus = models.BooleanField(default=True)
		
		def __str__(self):
				return str(self.valor)

class Personas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    estado = models.ForeignKey(cat_Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(cat_Municipio, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)

class Solicitudes(models.Model):
    descripcion = models.CharField(max_length=600)
    request_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.IntegerField()
    long = models.IntegerField()
    requested_datetime = models.DateTimeField()
    status = models.CharField(max_length=10)
    media_url = models.CharField(max_length=500, null=True, blank=True)
    agency_responsible = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.request_id)