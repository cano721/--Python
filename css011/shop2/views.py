from django.shortcuts import render

# Create your views here.

def userlist(request):
    rsuserlist = [
        {'id':'id01','pwd':'pwd01','name':'james01'},
        {'id':'id02','pwd':'pwd02','name':'james02'},
        {'id':'id03','pwd':'pwd03','name':'james03'},
        {'id':'id04','pwd':'pwd04','name':'james04'},
        {'id':'id05','pwd':'pwd05','name':'james05'}
    ]
    context = {
        'section':'userlist',
        'rsusers': rsuserlist
    }
    return render(request,'shop2/shop2.html',context)

def userdetail(request):
    id = request.GET['id']
    rsuser = {'id':id,'pwd':'pwd99','name':'이말숙'}
    context = {
        'section':'userdetail',
        'rsuser': rsuser
    }
    return render(request,'shop2/shop2.html',context)

def useradd(request):
    context = {
        'section':'useradd'
    }
    return render(request,'shop2/shop2.html',context)

def useraddimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    rsuser = {
        'id':id, 'pwd':pwd,'name':name
    }
    context = {
        'section':'userdetail',
        'rsuser': rsuser
    }
    return render(request,'shop2/shop2.html',context)

def itemlist(request):
    context = {
        'section':'itemlist'
    }
    return render(request,'shop2/shop2.html',context)

def itemadd(request):
    context = {
        'section':'itemadd'
    }
    return render(request,'shop2/shop2.html',context)
