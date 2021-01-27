from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def table(request):
    return render(request,'page/table.html')

def resume(request):
    return render(request,'page/resume.html')

def multi(request):
    return render(request,'page/multi.html')
