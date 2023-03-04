from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def about_view(request):
    return render(request, 'core/about.html')