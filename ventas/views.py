from cmath import exp
from itertools import product
from multiprocessing import context
from re import A, template
from urllib import response
from django.shortcuts import render, redirect
from .models import Personas, Producto, Solicitudes, cat_Municipio
from django.http import JsonResponse
from django.views import View
from ventas.forms import ProductoForm, LoginForm, FiltroProductoForm, PersonasForm
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from ventas.decorators import user_has_group, print_hello
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import json
from django.db.models import Q
from datetime import datetime 
from django.core.paginator import Paginator


class Index(View):
    template_name="ventas/ventas_index.html"
    context={}
    @method_decorator(cache_page(60 * 4))
    def get(self, request):
        solicitudes = Solicitudes.objects.all()

        page_size = 10
        page = 1

        results = Paginator(solicitudes, page_size)
        result = results.page(page)

        print(result)
        self.context['solicitudes'] = result
        self.context['last'] = results.num_pages
        
        self.context['next_page_number'] = result.next_page_number() if result.has_next() else ''
        self.context['previous_page_number'] = result.previous_page_number() if result.has_previous() else ''

        return render(request, self.template_name, self.context)

    def post(self, request):
        solicitudes = Solicitudes.objects.all()

        page_size = request.POST.get('page_size')
        page = request.POST.get('page')
        results = Paginator(solicitudes, page_size)
        result = results.page(page)

        print(result)
        self.context['solicitudes'] = result
        self.context['last'] = results.num_pages
        self.context['page_size']=page_size
        if result.number == 1:
            pag =  range(result.number, result.number+5)
        elif result.number == 2:
            pag =  range(result.number - 1, result.number+4)
        elif result.number == results.num_pages:
            pag =  range(result.number - 4, result.number+1)
        elif result.number == results.num_pages-1:
            pag =  range(result.number - 3, result.number+2)

        else:
            pag =  range(result.number - 2, result.number+3)
        self.context['paginas'] = pag

        
        self.context['next_page_number'] = result.next_page_number() if result.has_next() else ''
        self.context['previous_page_number'] = result.previous_page_number() if result.has_previous() else ''

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

@print_hello("Daniel")
def eliminar_producto(request):
    print("estamos eliminando el registro...")

    response={}

    id = request.POST.get('id')
    
    producto = Producto.objects.get(pk=id)
    producto.activo = False
    producto.save()
    response['id'] = producto.pk
    
    
    return JsonResponse(response)

def filtro_productos(request):
    response = {}
    q = Q(pk__isnull = False)

    nombre = request.POST.get('nombre')
    precio_min = request.POST.get('precio_min')
    precio_max = request.POST.get('precio_max')
    activo = request.POST.get('activo')

    if nombre is not "" and nombre is not None:
        q &= Q(nombre__icontains = nombre)

    if precio_max is not "" and precio_max is not None and precio_min is not "" and precio_min is not None:
        q &= Q(precio__gte = precio_min, precio__lte = precio_max)
    elif precio_max is not "" and precio_max is not None:
        q &= Q(precio__lte = precio_max)
    elif precio_min is not "" and precio_min is not None:
        q &= Q(precio__gte = precio_min)
    if activo == "true":
        q &= Q(activo = True)
    else: 
        q &= Q(activo = False)

    productos = Producto.objects.filter(q)
    dict_productos = {}
    for producto in productos:
        archivo_nombre = ""
        archivo_url = ""
        if producto.archivos:
            archivo_nombre = producto.archivos.name
            archivo_url = producto.archivos.url
        data = {
            "{}".format(producto.id):{
                "nombre":producto.nombre,
                "descripcion":producto.descripcion,
                "precio":producto.precio,
                "archivo_nombre":archivo_nombre,
                "archivo_url":archivo_url,
                "activo":producto.activo,

            }
        }
        dict_productos.update(data)

    response["productos"] = dict_productos

    return JsonResponse(response)

class ProductosView(View):
    context={}
    template_name="ventas/productos.html"
    def get(self, request):
        
        self.context["formProductos"] = ProductoForm()
        self.context["formProductosFiltro"] = FiltroProductoForm()

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
        self.context["formProductosFiltro"] = FiltroProductoForm()



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

def graficas(request):
    context={}
    template_name = "ventas/graficas.html"
    dic = datetime(2021, 12, 31)
    enero = datetime(2021, 1, 1)
    month_before = 1
    count = 0
    meses = [0,0,0,0,0,0,0,0,0,0,0,0]

    solicitudes = Solicitudes.objects.filter(requested_datetime__gte=enero, requested_datetime__lte=dic).order_by('requested_datetime')
    for solicitud in solicitudes:
        if solicitud.requested_datetime.month != month_before:
            count += 1

        meses[count] += 1

        month_before = solicitud.requested_datetime.month
    print(meses)
    context['meses']=meses

    return render(request, template_name, context)



def logoutCustom(request):
    logout(request)
    return redirect('login')

def filtrar_estados(request):
    response = {}
    municipios_dict=[]

    id_estado = request.POST.get('id_estado')
    municipios = cat_Municipio.objects.filter(cat_entidades_federativas = id_estado)

    for municipio in municipios:
        data = {
                "id":municipio.pk,
                "nombre":municipio.valor
            }

        municipios_dict.append(data)

    print(municipios_dict)

    response["municipios"] = municipios_dict

    return JsonResponse(response)

def perfil_view(request):
    
    template_name = "ventas/perfil.html"
    context ={}
    context['personasForm'] = PersonasForm()

    return render(request, template_name, context)

def solicitud(request):
    context = {}
    for page in range(1,11):

        data = {
            "lat":41.3083,
            "long":-72.9279,
            "page_size":100,
            "page":page    
        }
        r = requests.get('https://seeclickfix.com/open311/v2/requests.json/', data=data)
        response = json.loads(r.content)
        

        for resp in response:
            try:
                if not Solicitudes.objects.filter(request_id=resp['service_request_id']).exists():
                    solicitud = Solicitudes(descripcion=resp['description'], request_id=resp['service_request_id'], address=resp['address'],
                                            lat=resp['lat'],long=resp['long'],requested_datetime=resp["requested_datetime"],status=resp['status'],
                                            media_url=resp["media_url"],agency_responsible=resp["agency_responsible"])
                    solicitud.save()
            except Exception as e:
                print(str(e))
        
    context['response'] = response


    

    return JsonResponse(context)
