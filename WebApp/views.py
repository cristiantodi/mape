from django.shortcuts import render

from carro.carro import Carro

# Create your views here.

def home(request):
    
    carro=Carro(request)
    return render(request,"WebApp/home.html")

