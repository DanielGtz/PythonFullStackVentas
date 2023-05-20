from dataclasses import field
from socket import fromshare
from django import forms
from ventas.models import Producto
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

class LoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))
     


