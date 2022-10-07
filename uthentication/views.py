from contextlib import _RedirectStream, redirect_stderr, redirect_stdout
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import user
from django.contrib import messages
from django.contrib.auth import authenticate
from django import login

# Create your views here.
def home(request):
      return render(request,'uthentication/index.html') 

def details(request):
    if request.method=="post":
        patient=request.post['patient']
        doctor=request.post['doctor']


def  signup(request):
    if request.method=='post':
        fname=request.post['fname']
        lname=request.post['lname']
        username=request.post['username']
        emailid=request.post['emalid']
        pass1=request.post['pass1']
        paas2=request.post['pass2']
        Address=request.post['line'],['city'],['state']
        myuser =user.objects.create_user(username,emailid,pass1,)
        myuser.first_name=fname
        myuser.last_name=lname
    
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect_stderr('signin')

def signin(request):

    if request.method=="post":
        username=request.post['username']
        password=request.post['pass1']
        user=authenticate(username='username',password='pass1')
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"uthentiction/index.html",{'fname':fname})
        else:
            messages.error(request,"bad credentials!")
            return redirect_stderr('home')
    return render(request,"authentification/signin")
 



def signout(request):
    logout(request)
    messages.success(request,"logged out sucessfully!")
    return redirect_stderr('home')
