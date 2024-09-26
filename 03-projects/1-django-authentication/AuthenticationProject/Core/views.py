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

        try:
            user = User.objects.get(email=email)
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse("reset-password", kwargs={"reset_id":new_password_reset.reset_id})
            email_body = f"Reset your password using the link below:\n\n\n{password_reset_url}"

            email_message = EmailMessage(
                "Reset your password",
                email_body,
                settings.EMAIL_HOST_USER,
                [email]
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect("password-reset-sent", reset_id = new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with email {email} found")
            return redirect( "forgot-password")

    return render(request, "forgot_password.html")

def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):
    return render(request, "reset_password")




