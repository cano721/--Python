from django.shortcuts import render

# Create your views here.

def login(request):
    id = request.GET['id'];
    pwd = request.GET['pwd'];
    if id == 'qqq' and pwd == '111':
        context = {
            'loginid':id
        };
        return render(request, 'ok.html',context);
    else:
        return render(request,'fail.html')