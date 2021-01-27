from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'user/register.html')

def multi(request):
    return render(request,'multi.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def page4(request):
    return render(request,'page4.html')

def page5(request):
    return render(request,'page5.html')