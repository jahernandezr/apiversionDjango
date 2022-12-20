from django.shortcuts import render, redirect
#from .form import RegistrationForm
from .models import Account #, Vwmodulosaccesoview
from  django.contrib import messages, auth
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            emails = request.POST['email']
            # respuesta = Vwmodulosaccesoview.objects.filter(email = emails)

            auth.login(request, user)
            return redirect('inventario')
        else:
            messages.error(request,'credenciales incorrectas')
            return redirect('login')

    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has salido  de session')

    return redirect('login')
