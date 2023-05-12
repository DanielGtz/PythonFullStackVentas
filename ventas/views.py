from itertools import product
from re import template
from urllib import response
from django.shortcuts import render
from .models import Productos
from django.http import JsonResponse
from django.views import View

def index(request):
    context={}
    template_name="ventas/ventas_index.html"

    return render(request, template_name, context)

def editar_productos(request):

    response={}

    id = request.POST.get('id')
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    precio = request.POST.get('precio')
    producto = Productos.objects.get(pk=id)
        
    producto.nombre=nombre
    producto.descripcion=descripcion
    producto.precio=precio

    producto.save()
    response['id'] = producto.id
    response['nombre'] = producto.nombre
    response['descripcion'] = producto.descripcion
    response['precio'] = producto.precio
    
    return JsonResponse(response)

def eliminar_producto(request):

    response={}

    id = request.POST.get('id')
    
    producto = Productos.objects.get(pk=id)
    producto.activo = False
    producto.save()
    response['id'] = producto.pk
    
    
    return JsonResponse(response)


class ProductosView(View):
    context={}
    template_name="ventas/productos.html"
    def get(self, request):
        productos = Productos.objects.filter(activo=True)
        self.context["productos"] = productos

        return render(request, self.template_name, self.context)

    def post(self, request):
        nombre = request.POST.get('nombresasda')
        nombre = request.POST.get('name')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        
        producto = Productos(nombre=nombre, descripcion=descripcion, precio=precio)
        producto.save()

        productos = Productos.objects.filter(activo=True)
        self.context["productos"] = productos


        return render(request, self.template_name, self.context)
