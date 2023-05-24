from django  import forms
from .models import Vehiculo, Propietario, Placa


class vehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class":"form-control"
            })

class propietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = "__all__"

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class":"form-control"
            })

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["NIV","noMotor","marca","linea","modelo"]

class PropietarioForm(forms.ModelForm):
    apPaterno = forms.CharField(label="Apellido Paterno")
    apMaterno = forms.CharField(label="Apellido Materno")

    class Meta:
        model = Propietario
        fields = ["RFC","nombre","apPaterno","apMaterno","apMaterno","email","CURP","calle","colonia","municipio","CP","edad"]


class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields = ["numero","numTC","vehiculo","propietario","estatus","oficina"]
