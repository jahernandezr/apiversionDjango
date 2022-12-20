
from django.shortcuts import render,redirect
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from .models import Inventario,Prestadoressuludvida,Vwmodulosaccesoview
from .forms  import Orderform
import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
@login_required()
def viewinventario(request):
    return render(request,'inventario/inventario.html')

def insertinventario(request):
    form = Orderform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('inventario')
    return render(request, 'inventario/inventario.html', {'form': form})
def buscarnitall(request):
    invet = Prestadoressuludvida.objects.all().values_list()
    responseData = { 'status': 'success', 'msg' : list(invet)}
    return JsonResponse(responseData)

def buscarnit(request):
    nit = request.POST['nitprestador']
    nits = Prestadoressuludvida.objects.filter(nitprestador=nit)
    resultado = serializers.serialize('json', nits)
    # aList = json.dumps(resultado)
    return HttpResponse(resultado, content_type="application/json")

def buscarmodulos(request):
    email = request.POST['inputemail']
    respuesta = Vwmodulosaccesoview.objects.filter(email = email)
    #respuesta = Vwmodulosaccesoview.objects.all()
    data = serializers.serialize('json', respuesta)
    return HttpResponse(data, content_type="application/json")

    #resultado = serializers.serialize('json', nits)
    #return JsonResponse({'resultado': resultado}) #JsonResponse({'nits': resultado}, safe=False)
    #queryset = Prestadoressuludvida.objects.filter(nitprestador=request.POST['nitprestador']).values()
    #return JsonResponse({"models_to_return": list(queryset)})
#    return HttpResponse(json.dumps(queryset), content_type="application/json")

# def getPhotos(request):
#     code = request.POST.get('code', '')
#     fotos = Photo.objects.filter(photoCode=code)
#     resultado = serializers.serialize('json', fotos)
#     return JsonResponse({'fotos': resultado}, safe=False)

    # datos = Inventario.objects.filter(user=current_user)
    # if request.method == 'POST':
    #     form = Orderform(request.POST)
    #     if form.is_valid():
    #         data = Inventario()
    #         data.tiporecobro = form.cleaned_data['tiporecobro']
    #         data.regimen = form.cleaned_data['regimen']
    #         data.descripcionrecobro = form.cleaned_data['descripcionrecobro']
    #         data.numerofactura_recobro = form.cleaned_data['numerofactura_recobro']
    #         data.nitprestador = form.cleaned.data['nitprestador']
    #         data.nombreprestador = form.cleaned.data['nombreprestador']
    #         data.fechaprestacion = form.cleaned.data['fechaprestacion']
    #         data.departamento = form.cleaned.data['departamento']
    #         data.municipio = form.cleaned.data['municipio']
    #         data.tipodocumentousuario = form.cleaned.data['tipodocumentousuario']
    #         data.identificacionusuario = form.cleaned.data['identificacionusuario']
    #         data.codtecnologia = form.cleaned.data['codtecnologia']
    #         data.nombretecnologia = form.cleaned.data['nombretecnologia']
    #         data.cantidad = form.cleaned.data['cantidad']
    #         data.valorunit = form.cleaned.data['valorunit']
    #         data.valfacturado = form.cleaned.data['valfacturado']
    #         data.numeromipres_actactc = form.cleaned.data['numeromipres_actactc']
    #         data.save()
    #         # return redirect('inventario')
    #     else:
    #         return render(request,'inventario/inventario.html')
