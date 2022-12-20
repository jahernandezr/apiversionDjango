from django.db import models
from dbview.models import DbView

# Create your models here.

class Inventario(models.Model):
    tiporecobro = models.CharField(db_column='tipoRecobro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regimen = models.CharField(db_column='Regimen', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcionrecobro = models.CharField(db_column='DescripcionRecobro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numerofactura_recobro = models.CharField(db_column='NumeroFactura_recobro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nitprestador = models.IntegerField(db_column='NitPrestador', blank=True, null=True)  # Field name made lowercase.
    nombreprestador = models.CharField(db_column='Nombreprestador', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaprestacion = models.DateField(db_column='FechaPrestacion', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=80, blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='Municipio', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tipodocumentousuario = models.CharField(db_column='TipoDocumentoUsuario', max_length=40, blank=True, null=True)  # Field name made lowercase.
    identificacionusuario = models.CharField(db_column='IdentificacionUsuario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codtecnologia = models.CharField(db_column='CodTecnologia', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombretecnologia = models.CharField(db_column='NombreTecnologia', max_length=400, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    valorunit = models.IntegerField(db_column='Valorunit', blank=True, null=True)  # Field name made lowercase.
    valfacturado = models.IntegerField(db_column='Valfacturado', blank=True, null=True)  # Field name made lowercase.
    numeromipres_actactc = models.CharField(db_column='NumeroMipres_ActaCtc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='username', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'

    def __str__(self):
        return self.numerofactura_recobro
        #return '{}{}'.format(self.nitprestador, self.nombreprestador)
class Prestadoressuludvida(models.Model):
    nitprestador = models.IntegerField()
    nombreprestador = models.CharField(max_length=400)

    def __str__(self):
        return self.nombreprestador

class Vwmodulosaccesoview(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    nombremodulo = models.CharField(db_column='nombremodulo', max_length=100)
    urlaplicativo = models.CharField(db_column='urlaplicativo', max_length=100)
    email = models.CharField(db_column='email', max_length=100)

    class  Meta:
        managed = False
        db_table = 'vwmodulosacceso'
