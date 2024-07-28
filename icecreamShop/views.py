from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'icecreamShop/index.html')

def about(request):
    return render(request,'icecreamShop/about.html')

def contact(request):
    return render(request,'icecreamShop/contact.html')

def shop(request):
    return render(request,"icecreamShop/shop.html")

def profile(request):
    return render(request,"icecreamShop/profile.html")

def cart(request):
    return render(request,"icecreamShop/cart.html")