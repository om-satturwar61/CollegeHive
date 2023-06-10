from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html')

def properties(request):
    return render(request,'properties.html')


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def bharatmata(request):
    return render(request,'bharatmata-society.html')