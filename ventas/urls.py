from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login', views.LoginCustomView.as_view(), name='login'),
    path('logout', views.logoutCustom, name='logout'),
    path('servidor', views.ServidorViews.as_view(), name='servidor'),
    path('productos', views.ProductosView.as_view(), name='productos'),
    path('solicitud', views.solicitud, name='solicitud'),
    path('perfil', views.perfil_view, name='perfil'),
    path('ajaxEditarProductos', views.editar_productos, name='ajaxEditarProductos'),
    path('ajaxEliminarProductos', views.eliminar_producto, name='ajaxEliminarProductos'),
    path('ajaxFiltro', views.filtro_productos, name='ajaxFiltro'),
    path('ajaxFiltarEstados', views.filtrar_estados, name='ajaxFiltarEstados'),
    path('graficas', views.graficas, name='graficas'),

]