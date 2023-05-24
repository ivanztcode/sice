from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homeCatalogos, name="homeCatalogos"),
    path("oficina/listar",views.oficinaListar, name="oficinaListar"),
    path("vehiculos/ver/",views.vehiculosVer, name="vehiculosVer"),
    path("vehiculos/crear/",views.vehiculosCrear, name="vehiculosCrear"),
    path("vehiculos/delete/",views.vehiculosDelete, name="vehiculosDelete"),
    path("vehiculos/update/",views.vehiculosUpdate, name="vehiculosUpdate"),

    path("propietarios/listar",views.propietariosListar, name="prpietariosListar"),
    path("propietarios/crear",views.propietariosCrear, name="propietariosCrear"),
    path("propietarios/ver",views.propietariosVer, name="propietariosVer"),

    path("placas/crear",views.placasCrear, name="placasCrear"),
    path("placas/ver",views.placasVer, name="placasVer"),
    path("placas/editar/<int:id>",views.placasUpdate,name="placasUpdate"),
    path("placas/eliminar/<int:pk>",views.placasEliminar,name="placasEliminar"),





]
