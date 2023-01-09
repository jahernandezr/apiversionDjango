from django import forms
from .models import RecobrosDetalle

class Orderformrecobro(forms.ModelForm):
    class Meta:
        model = RecobrosDetalle
        fields = ['tipodoc','numdocumento','numactaCtc','feacta','facturaips','fechaPrestacion','codtecnologia','nitprestador','cie10','cantidad','valorunit','valfacturado','copago','valliquidado','codhomologo','valorunith','valorhomologo','idsuministro','radanterior','itemanterior','radicadoApf','feauditoria','numfallo','fefallo','numAutoridadJudicial','tipoautoridadjudicial','codcausal','codigodane','idusuario','deschomologo','desctecnologia','tipoTecnologia']


# class formvwmodulosacceso(forms.ModelForm):
#     class Meta:
#         model = Vwmodulosaccesoview
#         fields = ['nombremodulo','urlaplicativo','email']
