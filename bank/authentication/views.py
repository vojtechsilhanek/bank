from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . formular import *
from django.shortcuts import render, redirect # přidáme redirect
from django.contrib.auth.forms import *

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "authentication/users.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "authentication/login.html", {
                "message": "invalid"
            })
    

    return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return render(request, "authentication/login.html", {
        "message": "Logged out."
    }) 



def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
    else:
        form = RegistrationForm()
    
    return render(request, "authentication\sign_up.html", {
        "form":form
        })