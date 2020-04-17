from django.shortcuts import render, redirect
from .models import Blog, Gitpost
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views


def article_list(request):
    article = Blog.objects.order_by('date')
    gitpost = Gitpost.objects.order_by('date')
    context = {
        'articles': article,
        'gitposts': gitpost,
    }

    return render(request, "DC_blog/article_list.html", context)


def article_detail(request, slug):
    article = Blog.objects.get(slug=slug)

    context = {
        'article': article,

    }
    return render(request, "DC_blog/article_detail.html", context)

@login_required(login_url='login')
def link_repo(request):
    if request.method == "POST":
        form = forms.CreateRepo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save()
            return redirect("list")
    else:
            form = forms.CreateRepo()
    return render(request, "DC_blog/link_repo.html", {"form": form})

@login_required(login_url='login')
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save()
            return redirect("list")
    else:
        form = forms.CreateArticle()
    return render(request, "DC_blog/article_create.html", {"form": form})
