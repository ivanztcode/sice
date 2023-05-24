from django.db import models
# La declaración `from django.core.exceptions import ValidationError` está importando la clase
# `ValidationError` del módulo `django.core.exceptions`. Esta clase se usa para generar un error de
# validación cuando el método `clean()` de un modelo falla al validar un campo.
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


    
class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()
    notas = models.TextField(blank=True)
        # Validar si ya existe un proveedor con el mismo nombre
    def clean(self):
        # Validar si ya existe un proveedor con el mismo nombre solo al guardar un proveedor nuevo
        if self._state.adding and Proveedor.objects.filter(nombre=self.nombre).exists():
            raise ValidationError(f"Ya existe un proveedor con el nombre: '{self.nombre}'. Por favor, elige un nombre diferente.")
        
    def __str__(self):
        return self.nombre
    

CATEGORIAS_CHOICES = (
    ('analgesicos','Analgésicos'),
    ('antibioticos','Antibióticos'),
    ('antiinflamatorios','Antiinflamatorios'),
    ('antidepresivos','Antidepresivos'),
    ('antialergicos','Antialérgicos'),
    ('antidiabeticos','Antidiabéticos'),
    ('antihistaminicos','Antihistamínicos'),
    ('anticoagulantes','Anticoagulantes'),
    ('anticonvulsivantes','Anticonvulsivantes'),
    ('antiespasmodicos','Antiespasmódicos'),
    ('antipireticos','Antipiréticos'),
    ('antitusivos','Antitusivos'),
    ('broncodilatadores','Broncodilatadores'),
    ('cardiotonicos','Cardiotónicos'),
    ('descongestionantes','Descongestionantes'),
    ('diureticos','Diuréticos'),
    ('hipnoticos','Hipnóticos y sedantes'),
    ('hormonas','Hormonas'),
    ('analgesicos','Inhibidores de la bomba de protones'),
    ('laxantes','Laxantes'),
    ('relajantes','Relajantes musculares'),
    ('vitaminas','Vitaminas y suplementos'), 
)

MARCA_CHOICES = [
   ('pfizer', 'Pfizer'),   
   ('bayer', 'Bayer'),    
   ('roche', 'Roche'),    
   ('novartis', 'Novartis'),    
   ('merck', 'Merck'),   
   ('sanofi', 'Sanofi'),    
   ('glaxosmithkline', 'GlaxoSmithKline'),    
   ('johnsonjohnson', 'Johnson & Johnson'),    
   ('abbott', 'Abbott'),    
   ('eli lilly', 'Eli Lilly'),    
   ('astrazeneca', 'AstraZeneca'),    
   ('bristolmyerssquibb', 'Bristol-Myers Squibb'),    
   ('teva', 'Teva'),    ('sandoz', 'Sandoz'),    
   ('mylan', 'Mylan'),    
   ('abbvie', 'AbbVie'),    
   ('amgen', 'Amgen'),    
   ('biogen', 'Biogen'),    
   ('celgene', 'Celgene'),    
   ('gilead', 'Gilead'),    
   ('merckkgaa', 'Merck KGaA'),    
   ('allergan', 'Allergan'),    
   ('shionogi', 'Shionogi'),    
   ('takeda', 'Takeda'),    
   ('baxter', 'Baxter'),    
   ('merckco', 'Merck & Co.'),    
   ('bectondickinson', 'Becton, Dickinson and Company'),    
   ('daiichi sankyo', 'Daiichi Sankyo'),    
   ('gliead sciences', 'Gilead Sciences'),    
   ('grifols', 'Grifols'),    
   ('hikma', 'Hikma'),    
   ('lupin', 'Lupin'),    
   ('mallinckrodt', 'Mallinckrodt'),    
   ('myriad genetics', 'Myriad Genetics'),    
   ('pernod ricard', 'Pernod Ricard'),    
   ('pfenex', 'Pfenex'),    
   ('pharmacia', 'Pharmacia'),    
   ('pliva', 'Pliva'),    
   ('ptc therapeutics', 'PTC Therapeutics'),    
   ('ra pharma', 'Ra Pharma'),    
   ('santhera pharmaceuticals', 'Santhera Pharmaceuticals'),    
   ('sarepta therapeutics', 'Sarepta Therapeutics'),    
   ('sun pharmaceutical', 'Sun Pharmaceutical'),    
   ('taiho oncology', 'Taiho Oncology'),   
   ('tesaro', 'Tesaro'),    
   ('thermo fisher scientific', 'Thermo Fisher Scientific'),    
   ('tolero pharmaceuticals', 'Tolero Pharmaceuticals'),    
   ('xoma', 'Xoma'),    
   ('zoetis', 'Zoetis'),    
   ('zydus cadila', 'Zydus Cadila'),
]

PRESENTACION_CHOICES = [
    ('ampolla', 'Ampolla'),
    ('tableta', 'Tableta'),
    ('cápsula', 'Cápsula'),
    ('solución', 'Solución'),
    ('jarabe', 'Jarabe'),
    ('crema', 'Crema'),
    ('pomada', 'Pomada'),
    ('gel', 'Gel'),
    ('spray', 'Spray'),
    ('gotas', 'Gotas'),
    ('supositorio', 'Supositorio'),
    ('polvo', 'Polvo'),
    ('inyección', 'Inyección'),
    ('ovulo', 'Óvulo'),
    ('granulado', 'Granulado'),
    ('líquido', 'Líquido'),
    ('capsula blanda', 'Cápsula blanda'),
    ('comprimido', 'Comprimido'),
    ('efervescente', 'Efervescente'),
    ('suspensión', 'Suspensión'),
    ('enema', 'Enema'),
    ('parche', 'Parche'),
    ('espuma', 'Espuma'),
    ('línea nasal', 'Línea nasal'),
    ('chicle', 'Chicle'),
    ('spray nasal', 'Spray nasal'),
    ('polvo inhalado', 'Polvo inhalado'),
    ('tableta masticable', 'Tableta masticable'),
    ('tableta bucal', 'Tableta bucal'),
    ('polvo efervescente', 'Polvo efervescente'),
    ('polvo oral', 'Polvo oral'),
    ('solución oral', 'Solución oral'),
    ('suspensión oral', 'Suspensión oral'),
    ('inyección subcutánea', 'Inyección subcutánea'),
    ('inyección intramuscular', 'Inyección intramuscular'),
    ('inyección intravenosa', 'Inyección intravenosa'),
    ('inyección intravenosa lenta', 'Inyección intravenosa lenta'),
    ('inyección intravenosa en bolo', 'Inyección intravenosa en bolo'),
    ('inyección intraarterial', 'Inyección intraarterial'),
    ('inyección intracardiaca', 'Inyección intracardiaca'),
    ('inyección intradérmica', 'Inyección intradérmica'),
    ('inyección intraarticular', 'Inyección intraarticular'),
    ('implante', 'Implante'),
    ('cápsula oral de liberación prolongada', 'Cápsula oral de liberación prolongada'),
    ('tableta de liberación prolongada', 'Tableta de liberación prolongada'),
    ('tableta recubierta', 'Tableta recubierta'),
    ('gránulos para suspensión oral', 'Gránulos para suspensión oral'),
    ('crema vaginal', 'Crema vaginal'),
    ('gel vaginal', 'Gel vaginal'),
    ('óvulo vaginal', 'Óvulo vaginal'),
    ('solución inyectable', 'Solución inyectable'),
    ('solución para nebulizar', 'Solución para nebulizar'),
    ('solución oftálmica', 'Solución oftálmica'),
    ('crema para la piel', 'Crema para la piel'),
    ('solución auricular', 'Solución auricular'),
    ('aerosol', 'Aerosolo')
]



class Producto(models.Model):
    codigo_barras = models.CharField(max_length=50, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_caducidad = models.DateField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=70,choices=CATEGORIAS_CHOICES)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    marca = models.CharField(max_length=100, choices=MARCA_CHOICES)
    presentacion = models.CharField(max_length=100, choices=PRESENTACION_CHOICES)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    ubicacion = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    unidades = models.CharField(max_length=50)

    def save(self,*args, **kwargs):
        self.nombre_producto = self.nombre_producto.upper()
        super(Producto,self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo_barras + " - "+ self.nombre_producto
    

class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    impuesto_importe = models.FloatField(default=0)
    impuesto = models.FloatField(default=0)
    monto_ofrecido = models.FloatField(default=0)
    monto_cambio = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.code
    
    
class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)