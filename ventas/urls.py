from django.urls import path, re_path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.ProductosView.as_view(), name='productos'),
    path('ajaxEditarProductos', views.editar_productos, name='ajaxEditarProductos'),
    path('ajaxEliminarProductos', views.eliminar_producto, name='ajaxEliminarProductos'),
]