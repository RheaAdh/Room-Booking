from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import BookingList,AdminEditList
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    user=request.user
    admineditlist=user.admineditlist_set.all()
    return render(request,'accounts/dashboard.html',{'admineditlist':admineditlist})

def register(request):
    if request.method=="POST":
        form=CreateUser(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CreateUser()
    return render(request,'accounts/register.html',{'form':form})



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Credentials entered are wrong, please try again")
    return render(request,'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

    

