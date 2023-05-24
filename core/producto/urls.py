from django.urls import path,include
from . import views

urlpatterns = [
    path("producto/",views.productoCrear, name="addProducto"),
    path("proveedor",views.proovedorCrear, name="addProveedor"),
    path("/proveedor/ver/", views.verProveedor, name="verProveedor"),

]
