from django import forms
from .models import Producto, Proveedor
# `from django.core.validators import RegexValidator` está importando la clase `RegexValidator` del
# módulo `django.core.validators`. Esta clase se usa para validar que un campo coincide con un patrón
# de expresión regular específico. Se puede usar en formularios de Django para garantizar que la
# entrada del usuario coincida con un formato determinado.
from django.core.validators import RegexValidator


class ProductoForm(forms.ModelForm):
    codigo_barras = forms.CharField(
        label="Código de Barras", min_length=10, max_length=15,
        validators= [RegexValidator(r'^[0-9]+$',message = " Solo números están permitidas")],
        widget=forms.TextInput(attrs={'placeholder':'Ej: 1121334444   '})
    )
    nombre_producto = forms.CharField(
        label= "Nombre del producto", min_length=5,
        validators= [RegexValidator(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ\s]+$',message = " Solo números y letras están permitidas")],
        widget=forms.TextInput(attrs={'placeholder':'Ej: Aspirina'})
    )
    class Meta:
        model = Producto
        fields = ["codigo_barras","nombre_producto","descripcion","precio_compra","precio_venta","proveedor","fecha_caducidad","stock","categoria","imagen","marca","presentacion","descuento","ubicacion","unidades"]
        widgets = {
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "marca": forms.Select(attrs={"class": "form-control"}),
            "presentacion": forms.Select(attrs={"class": "form-control"}),
            "proveedor": forms.Select(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control","type":"file"}),

        }
        
class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(
        label ="Nombre del Proveedor",
        min_length=3,
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ\s]+$', message="Solo números y letras están permitidas")],    
        widget=forms.TextInput(attrs={'placeholder':'Ej: Farmacias ABC'})
    )

    direccion = forms.CharField(
        label = "Dirección del Proveedor",
        min_length=7,
        validators=[RegexValidator(r'^[A-Za-z0-9\s\-.,]+$', message="La dirección no es válida. Solo se permiten letras, números, espacios y los caracteres especiales: -, .")],    
        widget=forms.TextInput(attrs={'placeholder':'Ej: Av. Campeche 35 A. '})
    )

    correo_electronico = forms.CharField(
        label= "Correo electrónico",
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message="El correo electrónico no es válido."
            )
        ],
        widget=forms.EmailInput(attrs={'placeholder': 'Ej: ejemplo@dominio.com'})

    ) 
    class Meta:
        model = Proveedor
        fields = ["proveedor_id","nombre","direccion", "correo_electronico","telefono","pagina_web","notas"]

        widgets = {
            'telefono': forms.TextInput(
                attrs={
                    'style':'font-size: 13px',
                    'placeholder':'Telefono',
                    'data-mask': '(00) 000-000-00-00'
                }
            )
        }




