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
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Registration Successful")
                return HttpResponse("registration done")
    
    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html',context=context)

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponse('login done')
    else:
        form = LoginForm()
        
    context ={
        'form':form
    }
    return render(request,'accounts/login.html',context=context)