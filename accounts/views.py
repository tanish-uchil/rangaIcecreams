from django.shortcuts import render

# Create your views here.
def singupUser(request):
    return render(request,'accounts/signup.html')

def loginUser(request):
    pass