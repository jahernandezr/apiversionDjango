from django import forms
from .models import Inventario

class Orderform(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['tiporecobro', 'regimen' ,'descripcionrecobro','numerofactura_recobro','nitprestador','nombreprestador','fechaprestacion','departamento','municipio','tipodocumentousuario','identificacionusuario','codtecnologia','nombretecnologia','cantidad','valorunit','valfacturado','numeromipres_actactc','username']

# class formvwmodulosacceso(forms.ModelForm):
#     class Meta:
#         model = Vwmodulosaccesoview
#         fields = ['nombremodulo','urlaplicativo','email']
