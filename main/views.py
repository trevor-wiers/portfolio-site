from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "main/home.html")

def gritEQ(request):
    return render(request, "main/grit-eq.html")

def spectro(request):
    return render(request, "main/spectro.html")