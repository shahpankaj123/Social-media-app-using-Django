from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='Login')
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']
        password1=request.POST['pass1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already token')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already token')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user_model=User.objects.get(username=username)
                print(user_model.id)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('Login')       
        else:
            messages.info(request,'Password not matched')
            return redirect('signup')

    return render(request,'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password donot match')
            return redirect('Login')   
    return render(request,'signin.html')

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Login')
