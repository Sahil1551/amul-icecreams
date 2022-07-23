from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,details

from django.contrib.auth import login, logout, authenticate
# Create your views here.

def Details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'softy.html')
def Details_(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'bt.html')
def Details_2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'cb.html')
def Details_3(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'cc.html')


def Details_4(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request, 'cf.html')

def Details_5(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'ca.html')
def Details_6(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'m.html')
def Details_7(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'ra.html')
def Details_8(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        detail = details(name=name, email=email, phone=phone, add=add)
        detail.save()
        return render(request,'va.html')
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print(desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def ice(request):
    return render(request,'icecream.html')

def family(request):
    return render(request,'family.html')
def register(request):
    return render(request,'register.html')
def buy_butterscotch_cup(request):
    return render(request,'buy_butterscotch_cup.html')
def detail(request):
    return  render(request,'details.html')
def buy_chocolate_capucino(request):
    return render(request,'buy_chocolate_capucino.html')
def buy_vanilla_royale(request):
    return  render(request,'buy_vanilla_royale.html')
def buy_chocolate_brownie(request):
    return  render(request,'buy_chocolate_brownie.html')
def buy_chocolate_fudge(request):
    return render(request,'buy_chocolate_fudge.html')
def buy_creamy_almond(request):
    return render(request,'buy_creamy_almond.html')
def buy_roasted_almond(request):
    return render(request,'buy_roasted_almond.html')
def buy_morocon(request):
    return render(request,'buy_morocon.html')
def buy_butterscotch_tricone(request):
    return render(request,'buy_butterscotch_tricone.html')
def vr(request):
    return render(request,'details_vanilla_royale.html')
def bt(request):
    return render(request,'details_butterscotch_tricone.html')
def ca(request):
    return render(request,'details_creamy_almond.html')
def cb(request):
    return render(request,'details_choclate_brownie.html')
def cc(request):
    return render(request,'details_choclate_capucino.html')
def cf(request):
    return render(request,'details_chocolate_fudge.html')
def m(request):
    return render(request,'details_morocon.html')
def ra(request):
    return render(request,'details_roasted_almond.html')






















