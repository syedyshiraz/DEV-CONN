from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.





def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:

        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "account has been created " + user)
                return redirect("login")
    context = {"form": form}

    return render(request, "DC_app/register.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.info(request, "username and pasword is incorrect ")

    context = {}
    return render(request, "DC_app/login.html", context)


def logoutfield(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    dict = {"home_page": "Welcome to the home page"}
    return render(request, "DC_app/homePage.html", context=dict)
