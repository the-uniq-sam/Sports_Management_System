from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'Home_Page/registration.html')
