from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def docregister(request):
    return render(request,"docregister.html")

def doclogin(request):
    return render(request,"doclogin.html")

def patregister(request):
    return render(request,"patregister.html")

def patlogin(request):
    return render(request,"patlogin.html")

