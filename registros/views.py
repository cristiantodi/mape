from django.shortcuts import render

# Create your views here.

def registros(request):
    return render(request, "registros/registros.html")
