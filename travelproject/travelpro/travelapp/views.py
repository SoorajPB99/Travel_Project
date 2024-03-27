from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place


# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method== 'POST':
        name = request.POST['ticket-form-name']
        email = request.POST['ticket-form-email']
        tel = request.POST['ticket-form-phone']
        num = request.POST['ticket-form-number']
        addi = request.POST['ticket-form-message']
        if User.objects.filter(name=name).exista():
            messages.info(request,"name taken")
            return redirect('register')
        user=User.objects.create_user(username=name,email=email)
        user.save();
        return redirect('login')
        print("user created")

    return render(request,"register.html")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")