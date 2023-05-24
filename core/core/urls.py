from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name="index"),
    path("catalogos/",include("catalogos.urls")),
    path("agregar/",include("producto.urls")),

]
