from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')



    return render(request,"login.html")


def register(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(first_name=first_name).exists():
                messages.info(request,"first_name taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
               user = User(first_name=first_name, last_name=last_name, email=email, password=password)

            user.save();
            return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")