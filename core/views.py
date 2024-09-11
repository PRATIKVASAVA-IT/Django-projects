from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from .forms import user_signup

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=user_signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Use Created Successfully!')
            return HttpResponseRedirect('/login2/')

    fm=user_signup()
    return render (request,'reg.html',{'form':fm})

def user_login(request):
    return render(request,'log2.html')


