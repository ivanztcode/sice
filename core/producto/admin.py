from django.contrib import admin
from .models import Producto, Proveedor, Sales , salesItems
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['proveedor_id','nombre','direccion','correo_electronico','telefono','pagina_web','notas']
    search_fields = ['proveedor_id','nombre']
    list_per_page = 10




admin.site.register(Producto)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Sales)
admin.site.register(salesItems)