from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from schoolapp.forms import RegistrationForm, RegistrationsForm


# from schoolapp.forms import RegistrationForm


# Create your views here.
def demo(request):
    return render(request,'home.html')




# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'username taken')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save()
#                 return redirect('login')
#
#         else:
#             messages.info(request,'password not matching')
#             return redirect('register')
#
#
#
#
#
#
#     return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def new(request):
    return render(request,'new.html')
def form(request):
    # if request.method=='POST':
    #     print('user created')
    #     messages.info(request,'successfully added')
    # else:
    #     print("user not created")
    if request.method == 'POST':
        form1 = RegistrationsForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.info(request,'Registration successfully completed')
            return redirect('form')
    else:
        form1 = RegistrationsForm()

    return render(request,'newform.html',{'form1': form1})
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page.
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
