from ctypes import set_errno
import time
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from signupin.serializers import ReviewSerializers, StudSerializers
from .forms import Myreview, SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth 

# Create your views here.
from .models import *

def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "You are registered successfully")
            return redirect('signupin:signup')

    else:
        fm = SignupForm()
    return render(request,'signup.html',{'form':fm}) 

def review(request):
    if request.method == 'POST':
        fm = Myreview(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            myname = nm.upper()
            sb = fm.cleaned_data['subject']
            rv = fm.cleaned_data['review']
            hd = fm.cleaned_data['hidden']
            tk = fm.cleaned_data['tick']
            rev = Review(name = myname, subject = sb, review = rv, hidden = hd, tick = tk)
            rev.save()
            time.sleep(5)
            messages.success(request,'Your review has been Sent Successfully')
            return redirect('/')
    else:
        fm = Myreview()
    return render(request, 'review.html',{'form':fm})

def login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request = request, data = request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            # if username == email:

            pw = fm.cleaned_data['password']
            user = auth.authenticate(username = username, password = pw)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"You are logged in Successfully")
                return redirect('signupin:profile')
            else:
                messages.error(request,"Your are not registered")
    else:
        fm = AuthenticationForm()
    return render(request,'login.html', {'form':fm})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username = username,password = password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('signupin:profile')
#         # else:
#         #     messages.error(request,'wrong username or password')
#         #     return redirect('signupin:login')
#     else:
#         fm = AuthenticationForm()
#     return render(request,'login.html', {'form':fm})

from datetime import timedelta
def profile(request):
    user = request.user
    if user.is_authenticated:
        # date = MeroTime.objects.all()
        # {'mydate':date}
        # create_date = mydate.create_at
        # print(create_date)
        # n = 2
        # c_date = date.create_at[0]
        # final_date = c_date - timedelta(minutes=n)

        return render(request, 'profile.html')
    else:
        return redirect('signupin:signup')


def logout(request):
    auth.logout(request)
    return redirect('signupin:login')


# django rest framework start
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
@api_view(['GET', 'POST','PUT','PATCH', 'DELETE'])
def stud_api(request, pk = None):
    try:
        id = pk
        stu = Stud.objects.get(id = id)

    except :
        return Response(status= status.HTTP_404_NOT_FOUND)
        
    
    if request.method == 'GET':
        serializer = StudSerializers(stu)
        return Response(serializer.data)



    if request.method == "POST":
        serializer = StudSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"DAta Created!"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)

    
    if request.method == "PUT":
        # id = pk
        # stu = Stud.objects.get(id = id)
        serializer = StudSerializers(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Updated Using Put"}, status= status.HTTP_100_CONTINUE)
        return Response(serializer.errors)

    if request.method == "PATCH":
        # id = pk 
        # stu = Stud.objects.get(id = id)
        serializer = StudSerializers(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data crated using Patch"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        # id = pk
        # stu = Stud.objects.get(id = id)
        # serializer = StudSerializers(stu, data = request.data)
        stu.delete()
        return Response({'msg':"Data Deleted"})
    
