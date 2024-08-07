from django.shortcuts import render,redirect,HttpResponse
from accounts.forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from accounts.forms import UpdateUserForm
from accounts.models import Customer
# Create your views here.
def signupUser(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Registration Successful")
                return redirect('index')
    
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context=context)

def loginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('index')
            
    context ={
        'form':form,
    }
    return render(request,'accounts/login.html',context=context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def updateUser(request):
    updateForm = UpdateUserForm(request.POST,instance=request.user) 
    current_user = Customer.objects.get(id=request.user.id)
    if updateForm.is_valid():
        updateForm.save()
        login(request,request.user)
        messages.success(request,"Update Successful")
        return redirect('index')
    else:
        print(updateForm.errors)
        messages.warning(request,'Some error occured')
        return redirect('profile')