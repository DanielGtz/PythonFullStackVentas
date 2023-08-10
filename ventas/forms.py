from dataclasses import field
from socket import fromshare
from django import forms
from ventas.models import Producto, Personas
'''
class ProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa nombre del producto"}))
    descripcion = forms.CharField(label="Descripción detallada", widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Ingresa la descripción"}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa el precio"}))
'''
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre","descripcion","precio","archivos","activo"]
        widgets = {
            "nombre":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa nombre del producto"}),
            "descripcion":forms.Textarea(attrs={"class":"form-control","placeholder":"Ingresa la descripción"}),
            "precio":forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa el precio"}),
            "archivos":forms.FileInput(attrs={"class":"form-control"}),
            "activo":forms.CheckboxInput(),
        }

class FiltroProductoForm(forms.Form):
    nombre_filtro = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa nombre del producto"}))
    precio_min = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa el precio mínimo"}))
    precio_max = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa el precio máximo"}))
    activo_filtro = forms.IntegerField(widget=forms.CheckboxInput())

class LoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))
     
class PersonasForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ["usuario","nombre","apellidos","edad","calle","colonia","codigo_postal","estado","municipio"]
        widgets = {
            "usuario":forms.Select(attrs={'class': 'form-control'}),
            "nombre":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa tu nombre"}),
            "apellidos":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa tus apellidos"}),
            "edad":forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa tu edad"}),
            "calle":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa calle"}),
            "colonia":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa colonia"}),
            "codigo_postal":forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa codigo postal"}),
            "estado":forms.Select(attrs={'class': 'form-control'}),
            "municipio":forms.Select(attrs={'class': 'form-control'}),
        }

