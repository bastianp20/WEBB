from django.shortcuts import render 

def index(request):
    return render(request,'index.html')

def chat(request):
    return render(request,'chat.html') 

def perfil(request):
    return render(request,'perfil.html')

def apoyo (request):
    return render(request, 'apoyo.html')

def coins (request): 
    return render(request, 'coins.html')

def suscripciones(request):
    return render(request, 'suscripciones.html')