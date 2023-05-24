
from django.shortcuts import render,redirect

from .forms import ProductoForm,ProveedorForm
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Proveedor, Producto
import json, sys

# Create your views here.

# def productoCrear(request):
#     producto_form = ProductoForm()
#     if request.method == "POST":
#         producto_form = ProductoForm(data= request.POST)
#         if producto_form.is_valid():
#             producto_form.save()
#             messages.success(request,"Producto Agregado Exitosamente")
#             return redirect(reverse("addProducto")+"?ok")
#         else:
#             return redirect(reverse("addProducto")+"?error")
#     return render(request,"addProducto.html",{"form":producto_form})

def productoCrear(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Producto Agregado Exitosamente")
        return HttpResponseRedirect("/")
    context ={
        "form":form
    }
    return render(request,"addProducto.html",context)


# def proovedorCrear(request):
#     proovedor_form = ProveedorForm()
#     if request.method == "POST":
#         proovedor_form = ProveedorForm(data= request.POST)
#         if proovedor_form.is_valid():
#             proovedor_form.save()
#             messages.success(request,"Proveedor Agregado Exitosamente")
#             return redirect(reverse("addProveedor")+"?ok")
#         else:
#             return redirect(reverse("addProveedor")+"?error")
#     return render(request,"addProveedor.html",{"form":proovedor_form})

def proovedorCrear(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Proovedor Agregado Exitosamente")
        return HttpResponseRedirect("/")
    context ={
        "form":form
    }
    return render(request,"addProveedor.html",context)

def verProveedor(request):
    proveedor_list = Proveedor.objects.all()
    return render(request,"verProveedor.html",{"proveedores":proveedor_list})

def pos(request):
    products = Producto.objects.filter(stock__gte = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.id, 'name':product.name, 'price':float(product.price)})
    context = {
        'page_title' : "Point of Sale",
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    # return HttpResponse('')
    return render(request, "pos.html",context)
