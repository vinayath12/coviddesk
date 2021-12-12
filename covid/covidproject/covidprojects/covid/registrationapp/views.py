from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
           messages.info(request,'invalid username or password')
           return redirect('registrationapp:login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']

        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user exists")
                return redirect('registrationapp:register')
            elif User.objects.filter(password=password).exists():
                messages.info(request, "already exists")
                return redirect('registrationapp:register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                messages.info(request, "user created")
                return redirect('registrationapp:login')
        else:
             messages.info(request,"password not matching")
             return redirect('registrationapp:register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')