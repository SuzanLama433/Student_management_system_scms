from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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

        # Check if both passwords match
        if password == cpassword:

            # Check for unique username and email to avoid duplicate accounts
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already register')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already register')
                return redirect('register')

            # Check password strength

            # Method 1: Show individual error messages
            if not re.search("[A-Z]",password):
                messages.error(request,'your password must be contain at least one upper case')
                return redirect('register')
            if not re.search("\d",password):
                messages.error(request,'your password must be contain at least one digit')
                return redirect('register')

            # Method 2: Show a single combined error message
            # if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password):
            #     messages.error(request,'Invalid password')
            #     return redirect('log_in')

            # Validate the password using Django's built-in validators
            try:
                validate_password(password)
                User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    email=email,
                    password=password,
                )
                messages.success(request,'register successfuly')
                return redirect('log_in')
            except ValidationError as e:
                # Display all validation error messages
                for i in e.messages:
                    messages.error(request,i)
                return redirect('register')

        else:
            messages.error(request,'please Enter same password!!')
            return redirect('register')

    return render(request,'accounts/login.html')