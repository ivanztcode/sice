from django.shortcuts import render, redirect

from .models import Oficina, Vehiculo, Propietario, Placa
from .forms import propietarioForm,PropietarioForm, VehiculoForm, PlacaForm
from django.urls import reverse, reverse_lazy
from django.views import generic
# Create your views here.


def homeCatalogos(request):
    return render(request,"homeCatalogos.html")


def oficinaListar(request):
    pass

def vehiculosListar(request):
    pass



def vehiculosDelete(request):
    pass

def vehiculosUpdate(request):
    pass

def propietariosListar(request):
    pass



    
# def propietariosCrear(request):
#     if request.method == "POST":
#         form = PropietarioForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("propietariosCrear")
#     else:
#         form = PropietarioForm()
#     return render(request, "propietariosCrear.html", {"form": form})


def propietariosCrear(request):
    propietario_form = PropietarioForm()
    if request.method =="POST":
        propietario_form = PropietarioForm(data= request.POST)
        if propietario_form.is_valid():
            propietario_form.save()
            return redirect(reverse("propietariosCrear")+"?ok")
        else:
            return redirect(reverse("propietariosCrear")+"?error")
    return render (request,"propietariosCrear.html",{"form":propietario_form})

def propietariosVer(request):
    propietarios = Propietario.objects.all()
    return render(request,"propietariosVer.html",{"propietarios":propietarios})

def vehiculosCrear(request):
    vehiculos_crear = VehiculoForm()
    if request.method == "POST":
        vehiculos_crear = VehiculoForm(data=request.POST)
        if vehiculos_crear.is_valid():
            vehiculos_crear.save()
            return redirect(reverse("vehiculosCrear")+"?ok")
        else:
            return redirect(reverse("vehiculosCrear")+"?error")
    return render (request,"vehiculosCrear.html",{"form":vehiculos_crear})

def placasCrear(request):
    placas_crear=PlacaForm()
    if request.method =="POST":
        placas_crear= PlacaForm(data=request.POST)
        if placas_crear.is_valid():
            placas_crear.save()
            return redirect("propietariosCrear")

            # return redirect(reverse("placasCrear")+"?ok")
        else:
            return redirect(reverse("placasCrear")+"?error")
    return render(request,"placasCrear.html",{"form":placas_crear})


def placasView(request):
    pass

def placasVer(request):
    placas = Placa.objects.all()
    return render(request, "placasVer.html",{"placas":placas})

def placasUpdate(request, id):
    placas = Placa.objects.get(id=id)
    if request.method == "GET":
        form = PlacaForm(instance= placas)
    else:
        form = PlacaForm(request.POST, instance=placas)
        if form.is_valid():
            form.save()
            return redirect("placasVer")
    return render(request,"placasUpdate.html",{"form":form})

def placasEliminar(request,pk):
    placas = Placa.objects.get(pk=pk)
    if request.method == "POST":
        placas.delete()
        return redirect("placasVer")
    return render(request,"placasEliminar.html",{"placas":placas})








def vehiculosVer(request):
    vehiculos = Vehiculo.objects.all()
    return render(request,"vehiculosVer.html",{"vehiculos":vehiculos})



