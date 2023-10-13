from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

def home(request):
   
    return render(request,"index.html")
def login_page(request):
     if request.user.is_authenticated:
        return redirect('Home')
     else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect('Home')
            else:
                messages.error(request,"Invaild username or password")
                return redirect('login')
                
        return render(request,'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfuly")
        return redirect('Home')

@csrf_exempt
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Regirations successfully')
            return redirect('login')
    return render(request,"register.html",{'form':form})
