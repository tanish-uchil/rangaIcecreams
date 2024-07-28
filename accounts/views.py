from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def singupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html',context=context)

def loginUser(request):
    pass