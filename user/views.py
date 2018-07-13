from django.shortcuts import render

from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

import json

# Create your views here.
@login_required()
def info_user_view(request):
    user = request.user
    context = {
        'data':{
                'loged':'yes',
                'UserID':str(user.id),
                'UserName':user.username,
                'EmailAddress':user.email,
                'FirstName':user.first_name,
                'LastName':user.last_name,
        },
    }
    return render(request,'user/info/info.html',context)
    

def login_view(request):
    context = {}
    return render(request,'user/auth/login.html',context)

def login_api(request):
    def auth(user):
        # A backend authenticated the credentials
        login(request, user)
        context = {'error':'Not'}
        return HttpResponse(json.dumps(context), content_type="application/json")


        
    form = LoginForm(request.POST)
    #Form
    if form.is_valid():
        user_email = form.cleaned_data.get('user')
        password = form.cleaned_data.get('password')
        print(password)
        user = authenticate(username=user_email, password=password)
        if not user:
            #auth user with email
            try:
                username = User.objects.get(email=user_email).username
                user = authenticate(username=username, password=password)
                return auth(user)
            #No user
            except:
                # No backend authenticated the credentials
                try:
                    User.objects.get(username=user_email)
                    context = {'error':'password'}
                    return HttpResponse(json.dumps(context), content_type="application/json")
                except:
                    try:
                        User.objects.get(email=user_email)
                        context = {'error':'password'}
                        return HttpResponse(json.dumps(context), content_type="application/json")
                    except:
                        context = {'error':'user_email'}
                        return HttpResponse(json.dumps(context), content_type="application/json")
        #auth user with username
        else:
            return auth(user)

    
 
    #GET    
    else:
        user = request.user
        if user.is_authenticated:
            print('hola')

            context={
                'loged':'yes',
                'UserID':str(user.id),
                'UserName':user.username,
                'EmailAddress':user.email,
                'FirstName':user.first_name,
                'LastName':user.last_name,

            }
            print(context)
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            print('no user')
            context = {'loged':'not'}
            
                
            return HttpResponse(json.dumps(context), content_type="application/json")
@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
       
def error_api(request):
    #raise errors to analize it later
    return HttpResponseRedirect(reverse('inicio'))