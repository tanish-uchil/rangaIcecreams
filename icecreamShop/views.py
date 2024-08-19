from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import UpdateUserForm
from icecreamShop.models import Product,CartItem
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

# Create your views here.
def index(request):
    return render(request,'icecreamShop/index.html')

def about(request):
    return render(request,'icecreamShop/about.html')

def contact(request):
    return render(request,'icecreamShop/contact.html')

def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,"icecreamShop/shop.html",context=context)

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
    cart = CartItem.objects.filter(user=request.user)
    context = {
        'cart' : cart
    }
    return render(request,"icecreamShop/cart.html",context=context)

@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    item = CartItem(item=product,user=request.user)
    item.save()
    return redirect('cart') 