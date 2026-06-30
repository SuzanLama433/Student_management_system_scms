from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def log_in(request):
    
    return render(request,'accounts/login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            User.objects.create_user(first_name = fname, last_name = lname,username=username,email=email, password=password,)
            messages.success(request,'register successfuly')
            return redirect('log_in')
        else:
            messages.error(request,'please Enter same password!!')
            return redirect('register')

    return render (request,'accounts/login.html')