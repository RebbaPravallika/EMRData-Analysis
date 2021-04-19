from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")



def patregister(request):
    return render(request,"patregister.html")

def patlogin(request):
    return render(request,"patlogin.html")

def news(request):
    return render(request,"news.html")

def heart(request):
    return render(request,"heart.html")