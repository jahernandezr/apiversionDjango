from django.shortcuts import render,redirect
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from .models import RecobrosDetalle,InformacionUsuarios
from .forms  import Orderformrecobro
import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def getrecobros(request):
    return render(request, 'recobro/recobro.html')

def getnodocument(request):
    tipodoc = request.POST['tipodoc']
    numdocumento =request.POST['numdocumento']
    data = InformacionUsuarios.objects.filter(tipodoc=tipodoc, numdocumento=numdocumento)
    resultado = serializers.serialize('json', data)
    return HttpResponse(resultado, content_type="application/json")

def insertrecobros(request):
    form = Orderformrecobro(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        # return redirect('recobro')
    return render(request, 'recobro/recobro.html', {'form': form})
