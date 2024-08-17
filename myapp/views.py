
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
# Create your views here.
def home(request):
  return render(request,"home.html") 

def register(request):
    if request.method=="POST":
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      email=request.POST.get('email') 
      password1=request.POST.get('password1')
      password2=request.POST.get('password2')
      data=User.objects.create_user(first_name,last_name,username,email,password1)
      data.save()
    return render(request,'register.html')
    
def login(request):
  if request.method=="POST":
    username=request.POST['username']
    password=request.POST['password1']
    user = auth.authenticate(username=username,password1=password)
    if user is not None :
      auth.login(request,user)
      return render(request,'login.html')    
  return render(request,'login.html')    



def logout(request):
  logout(request)
  return redirect("/login")

