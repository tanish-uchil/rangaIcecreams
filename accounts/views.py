from django.shortcuts import render,redirect,HttpResponse
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        errors = form.errors
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Registration Successful")
                return redirect('index')
    
    form = SignUpForm()
    context = {
        'form': form,
        'error': errors
    }
    return render(request,'accounts/signup.html',context=context)

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Registration Successful")
                return redirect('index')
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username,password=password)
        # if user is not None:
        #     login(request,user)
        #     messages.success(request,"Login Successful")
        #     return redirect('index')
    else:
        form = LoginForm()
        
    context ={
        'form':form,
        'errors': form.errors
    }
    return render(request,'accounts/login.html',context=context)

def logoutUser(request):
    logout(request)
    return redirect('index')