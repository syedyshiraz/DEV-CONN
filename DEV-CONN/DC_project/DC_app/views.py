from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("list")
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

    return render(request, "register.html", context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')

        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('login')

    context = {}
    return render(request, 'login.html')


def logoutfield(request):
    logout(request)
    return redirect("list")


@login_required(login_url='login')
def home(request):
    dict = {"home_page": "Welcome to the home page"}
    return render(request, "homePage.html", context=dict)


@login_required(login_url='login')
def contact(request):
    return render(request,'team.html')
