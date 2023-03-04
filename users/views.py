from django.shortcuts import render

# Create your views here.
def client_login(request):
    return render(request, 'users/client_login.html')

def client_register(request):
    return render(request, 'users/client_register.html')

def acommodation_login(request):
    return render(request, 'users/acommodation_login.html')

def acommodation_register(request):
    return render(request, 'users/acommodation_register.html')