from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def first(request):

    return HttpResponse("hello world")


#   homepage

def home(request):

    return render(request,"home.html")


# signup page

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
           messages.info(request,"user name is already taken")
           return redirect("signup")

        if User.objects.filter(email=email).exists():
           messages.info(request,"email is already taken")
           return redirect("signup")

        else:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.set_password(password)
            user.save()
            messages.info(request,"user created successfully")
            return redirect("signin")

    return render(request,"register.html")


#  login page
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')


    return render(request,"login.html") 
def logout(request):
    auth.logout(request)
    messages.info(request,"you are signed out")
    return redirect("signin")
    










