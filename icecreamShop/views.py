from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import UpdateUserForm
from accounts.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

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
    current_user = request.user
    updateForm = UpdateUserForm(instance=current_user)
    context = {
        'updateForm': updateForm
    }
    return render(request,"icecreamShop/profile.html",context=context)

@login_required
def cart(request):
    return render(request,"icecreamShop/cart.html")