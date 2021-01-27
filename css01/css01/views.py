from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def test01(request):
    return render(request,'test01.html')

def test02(request):
    return render(request,'test02.html')

def test03(request):
    return render(request,'test03.html')