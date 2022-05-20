from django.shortcuts import render,redirect
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    return render(request,'core/home.html')
    

class SignupView(View):
    def get(self,request):
        fm=SignupForm()
        return render(request,'core/sign.html',{'form':fm})
    def post(self,request):
        fm=SignupForm(request.POST)
        if fm.is_valid():
           fm.save()
           messages.success(request,"Successfully registered")
           return redirect('/sign')
        else:
          return render(request,'core/sign.html',{'form':fm})
        
class Mylogin(View):
    def get(Self,request):
        fm=MyloginForm
        return render(request,'core/login.html',{'form':fm})
    def post(self,request):
        fm=MyloginForm(request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'core/login.html',{'form':fm})
        else:
            return render(request,'core/login.html',{'form':fm})

#course registration
class CourseRegistration(View):
     def get(self,request):

         fm1=RegisterForm()
         return render(request,'core/registration.html',{'form':fm1})
     def post(self,request):

         fm1=RegisterForm(request.POST)
         if fm1.is_valid():
               
             fm1.save()
             messages.success(request,"Successfully registered")
             return redirect('/')
         else:
            return render(request,'core/registration.html',{'form':fm1})
