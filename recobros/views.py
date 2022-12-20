from django.shortcuts import render,redirect
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from .models import RecobrosDetalle
# from .forms  import Orderform
import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def getrecobros(request):
    return render(request, 'recobro/recobro.html')
