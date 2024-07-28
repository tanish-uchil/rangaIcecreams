from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'icecreamShop/index.html')

def about(request):
    return render(request,'icecreamShop/about.html')

def contact(request):
    return render(request,'icecreamShop/contact.html')

def shop(request):
    return render(request,"icecreamShop/shop.html")

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,"icecreamShop/profile.html")

def cart(request):
    return render(request,"icecreamShop/cart.html")