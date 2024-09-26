from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

@login_required
def Home(request):
    return render(request, "index.html")

def RegisterView(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_has_data_error = False

        if User.objects.filter(username=username).exists():
            user_has_data_error = True
            messages.error(request, "Username already exists")
        
        if User.objects.filter(email=email).exists():
            user_has_data_error = True
            messages.error(request, "Email already exists")
        
        if len(password) < 5:
            user_has_data_error = True
            messages.error(request, "Password must be at least 5 characters")

        if user_has_data_error:
            return redirect("register")
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect("login")
        
    return render(request, "register.html")

def LoginView(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request=request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

def LogoutView(request):
    logout(request)
    return redirect("login")

def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
    return render(request, "forgot_password.html")

def PasswordResetSent(request, reset_id):
    return render(request,"password_reset_sent.html")

def ResetPassword(request, reset_id):
    return render(request, "reset_password")




