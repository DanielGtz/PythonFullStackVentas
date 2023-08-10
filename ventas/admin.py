from django.contrib import admin
from ventas.models import Personas, Producto, cat_Estado, cat_Municipio, Solicitudes


admin.site.register(Producto)
admin.site.register(Personas)
admin.site.register(cat_Estado)
admin.site.register(cat_Municipio)
admin.site.register(Solicitudes)
