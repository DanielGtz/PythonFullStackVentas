from itertools import product
from re import template
from urllib import response
from django.shortcuts import render, redirect
from .models import Personas, Producto
from django.http import JsonResponse
from django.views import View
from ventas.forms import ProductoForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ventas.decorators import user_has_group
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(View):
    template_name="ventas/ventas_index.html"
    context={}
    def get(self, request):
        return render(request, self.template_name, self.context)

class ServidorViews(View):
    template_name = "ventas/servidores.html"
    context={}
    @method_decorator(user_has_group('servidor'))
    def get(self,request):
        return render(request, self.template_name, self.context)
        
        
def editar_productos(request):

    response={}

    id = request.POST.get('id')
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    precio = request.POST.get('precio')
    producto = Producto.objects.get(pk=id)
        
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
    
    producto = Producto.objects.get(pk=id)
    producto.activo = False
    producto.save()
    response['id'] = producto.pk
    
    
    return JsonResponse(response)



class ProductosView(View):
    context={}
    template_name="ventas/productos.html"
    @method_decorator(user_has_group('ciudadano'))
    def get(self, request):
        productos = Producto.objects.filter(activo=True)
        self.context["productos"] = productos
        self.context["formProductos"] = ProductoForm()

        return render(request, self.template_name, self.context)
    @method_decorator(user_has_group('ciudadano'))
    def post(self, request):
        formP = ProductoForm(request.POST)
        if formP.is_valid():
            producto = formP.save(commit=False)
            archivos = request.FILES.get("archivos")
            print(archivos)
            producto.archivos = archivos
            producto.save()

        productos = Producto.objects.filter(activo=True)
        self.context["productos"] = productos
        self.context["formProductos"] = ProductoForm()


        return render(request, self.template_name, self.context)


class LoginCustomView(View):
    context={}
    template_name="ventas/login.html"
    def get(self, request):
        self.context["loginForm"] = LoginForm()
        self.context["error"]=""
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = LoginForm(request.POST)
        self.context["error"]=""
        if form.is_valid():
            usuario = form.cleaned_data.get("usuario")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                self.context["error"] = "Usuario inválido"
        self.context["loginForm"] = LoginForm()

        return render(request, self.template_name, self.context)


def logoutCustom(request):
    logout(request)
    return redirect('login')

    
def perfil_view(request):

    template_name = "ventas/perfil.html"
    context ={}

    persona = Personas.objects.get(usuario__pk=request.user.pk)
    context['persona'] = persona

    return render(request, template_name, context)
