from django.db import models

# Create your models here.
class Marca(models.Model):
    nombreMarca = models.CharField(max_length=50, verbose_name="Nombre de la marca")

    def __str__(self):
        return "%s"% (self.nombreMarca)


class Vehiculo(models.Model):
# Creando una tabla llamada Vehiculo con dos columnas: NIV y noMotor.
    NIV = models.CharField(max_length=20, help_text="NIV del vehiculo")
    noMotor =models.CharField(max_length=30,blank=True)
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    linea =  models.CharField(max_length=40)
    modelo = models.CharField(max_length=4)

    def __str__(self):
        return '%s - %s - %s' % (self.NIV,self.marca,self.linea)
    
    
    def save(self, *args, **kwargs):
        self.NIV = self.NIV.upper()
        self.noMotor = self.noMotor.upper()
        super(Vehiculo, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "VEHICULOS"
        db_table = 'vehiculo'


class Municipio(models.Model):
    nombreMunicipio = models.CharField(max_length=50, verbose_name="Nombre del municipio")

    def __str__(self):
        return "%s"% (self.nombreMunicipio)

class Propietario(models.Model):
    RFC = models.CharField(max_length=50)
    nombre = models.CharField(verbose_name="Nombre Completo" ,max_length=50)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    email = models.EmailField( max_length=40)
    CURP = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=40)
    municipio = models.ForeignKey(Municipio, on_delete = models.CASCADE)
    CP = models.CharField(max_length=5)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s %s %s" % (self.nombre, self.apPaterno, self.apMaterno)
    
    def save(self, *args, **kwargs):
        self.CURP = self.CURP.upper()
        super().save(*args, **kwargs)


class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=50, verbose_name="Nombre de Ciudad")

    class Meta:
        verbose_name_plural = "ciudades"


    def __str__(self):
        return "%s"% (self.nombreCiudad)

class Oficina(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return ("%s" % self.nombre)

class Placa(models.Model):
    numero = models.CharField(max_length=10)
    numTC = models.CharField(max_length=20)
    fecha = models.DateField(auto_now=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    propietario= models.ForeignKey(Propietario, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.numero, self.vehiculo)