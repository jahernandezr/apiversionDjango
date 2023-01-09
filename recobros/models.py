from django.db import models

# Create your models here.
# carlos montar las tablas de cie10,datos basicos del usuario, codigo y descripcion  de tecnologias, homologos
class RecobrosDetalle(models.Model):
    tipodoc = models.CharField(max_length=20)
    numdocumento = models.CharField(max_length=22)
    numactaCtc = models.CharField(max_length=40)
    feacta = models.DateField()
    facturaips = models.CharField(max_length=50)
    fechaPrestacion = models.DateField()
    codtecnologia = models.CharField(max_length=40)
    nitprestador = models.IntegerField()
    cie10 = models.CharField(max_length=7)
    cantidad = models.IntegerField()
    valorunit = models.IntegerField()
    valfacturado = models.IntegerField()
    copago = models.IntegerField()
    valliquidado = models.IntegerField()
    codhomologo = models.CharField(max_length=30, blank=True, null=True)
    valorunith = models.IntegerField(blank=True, null=True)
    valorhomologo = models.IntegerField(blank=True, null=True)
    idsuministro = models.IntegerField()
    radanterior = models.IntegerField()
    itemanterior = models.IntegerField()
    radicadoApf = models.IntegerField()
    feauditoria = models.DateField()
    numfallo = models.CharField(max_length=50, blank=True, null=True)
    fefallo = models.DateField( blank=True, null=True)
    numAutoridadJudicial = models.CharField(max_length=200, blank=True, null=True)
    tipoautoridadjudicial = models.CharField(max_length=200, blank=True, null=True)
    codcausal = models.IntegerField( blank=True, null=True)
    codigodane = models.CharField(max_length=10, blank=True, null=True)
    imgmipres = models.CharField(max_length=100, blank=True, null=True)
    imgctc = models.CharField(max_length=100, blank=True, null=True)
    imgfactura = models.CharField(max_length=100,blank=True, null=True)
    imgevidencia = models.CharField(max_length=100, blank=True, null=True)
    imgformula = models.CharField(max_length=100,blank=True, null=True)
    imgotros = models.CharField(max_length=100, blank=True, null=True)
    imgotros = models.CharField(max_length=100, blank=True, null=True)
    idusuario = models.IntegerField(blank=False, null=False)
    deschomologo = models.CharField(max_length=500,blank=True, null=True)
    desctecnologia = models.CharField(max_length=500, blank=True, null=True)
    tipoTecnologia = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.facturaips

class InformacionUsuarios(models.Model):
    tipodoc = models.CharField(max_length=20)
    numdocumento = models.CharField(max_length=22)
    primerNombre =models.CharField(max_length=100)
    segundoNombre =models.CharField(max_length=100)
    primerApellido =models.CharField(max_length=100)
    segundoApellido =models.CharField(max_length=100)
    tipoAfiliado = models.CharField(max_length=20)
    estadoAfiliacion = models.CharField(max_length=50)
    feInicio = models.DateField()
    fefinal = models.DateField()

    def __str__(self):
        return self.numdocumento

class Cie10(models.Model):
    codigoCie10 = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=350)

    def __str__(self):
        return self.descripcion

class ImagenesRecobros(models.Model):
    facturaips = models.CharField(max_length=40)
    nombreImagen = models.ImageField(upload_to='media/media/')
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __init__(self):
        return self.facturaips
