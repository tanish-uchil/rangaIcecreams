from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import UpdateUserForm

# Create your views here.
def index(request):
    return render(request,'icecreamShop/index.html')

def about(request):
    return render(request,'icecreamShop/about.html')

def contact(request):
    return render(request,'icecreamShop/contact.html')

def shop(request):
    return render(request,"icecreamShop/shop.html")

def updateUser(request):
    return render(request,'icecreamShop/index.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    updateForm = UpdateUserForm()
    context = {
        'updateForm': updateForm
    }
    return render(request,"icecreamShop/profile.html",context=context)

@login_required
def cart(request):
    return render(request,"icecreamShop/cart.html")