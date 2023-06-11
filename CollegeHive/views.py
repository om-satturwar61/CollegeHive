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

def garva(request):
    return render(request,'garva-girls-hostel.html')

def guruom(request):
    return render(request,'guru-om-hostel.html')

def gurukunj(request):
    return render(request,'gurukunj-hostel.html')

def harshraj_residency(request):
    return render(request,'harshraj-residency.html')

def mohanvilla(request):
    return render(request,'mohan-villa.html')

def sai_glamour(request):
    return render(request,'sai-glamour-residency.html')

def saptashrungi(request):
    return render(request,'saptashrungi-society.html')

def shree_ganesh_pg(request):
    return render(request,'shree-ganesh-pg.html')

def shree_pg_services(request):
    return render(request,'shree-pg-services.html')

def subhadra_hostel(request):
    return render(request,'subhadra-hostel.html')

