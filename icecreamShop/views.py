from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,"shop.html")

def profile(request):
    return render(request,"profile.html")

def cart(request):
    return render(request,"cart.html")