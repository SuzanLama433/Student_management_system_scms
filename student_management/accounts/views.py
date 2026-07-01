from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# User Login
def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check whether the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "username is not register yet")
            return redirect('log_in')

        # Authenticate the user using username and password
        checkAuth = authenticate(username=username, password=password)
        if checkAuth is not None:
            login(request, checkAuth)

            # Redirect to the originally requested page after successful login
            next = request.POST.get('next', '')
            return redirect(next if next else 'dashboard')
        else:
            messages.error(request, "invalid password")
            return redirect('log_in')

        # Alternative login using email instead of username
        # if request.method == "POST":
        #     email = request.POST.get("email")
        #     password = request.POST.get("password")

        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     user = None

        # if user:
        #     auth_user = authenticate(
        #         username=user.username,
        #         password=password
        #     )

        #     if auth_user is not None:
        #         login(request, auth_user)
        #         return redirect("dashboard")

        # messages.error(request, "Invalid email or password")

    # Store the requested URL so the user can be redirected after login
    next = request.GET.get('next', '')
    return render(request, 'accounts/login.html', {'next': next})


# User Registration
def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        terms = request.POST.get('terms')
        
        if not terms:
            messages.error(request,'You must agree to the Terms of Service and Privacy Policy.')
            return redirect('log_in')
        # Verify that password and confirm password match
        if password == cpassword:

            # Prevent duplicate username and email registration
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already register')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already register')
                return redirect('register')

            # Validate password strength

            # Method 1: Display separate validation messages
            if not re.search("[A-Z]", password):
                messages.error(request, 'your password must be contain at least one upper case')
                return redirect('register')

            if not re.search("\d", password):
                messages.error(request, 'your password must be contain at least one digit')
                return redirect('register')

            # Method 2: Validate password using a single regular expression
            # if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            #     messages.error(request, 'Invalid password')
            #     return redirect('log_in')

            # Validate the password using Django's built-in password validators
            try:
                validate_password(password)

                # Create a new user account
                User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    email=email,
                    password=password,
                )

                messages.success(request, 'register successfuly')
                return redirect('log_in')

            except ValidationError as e:
                # Display all password validation errors
                for i in e.messages:
                    messages.error(request, i)
                return redirect('register')

        else:
            # Password and confirm password do not match
            messages.error(request, 'please Enter same password!!')
            return redirect('register')

    return render(request, 'accounts/login.html')


# User Logout
def log_out(request):
    # Log out the currently authenticated user
    logout(request)

    # Redirect to the dashboard after logout
    return redirect('dashboard')