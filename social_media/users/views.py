from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        login(request, user)
        return redirect("feed")

    return render(request, "users/register.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("feed")

        return render(request, "users/login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request,"users/login.html")
