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


def link_repo(request):
    form = forms.CreateRepo()
    return render(request, "DC_blog/link_repo.html", {"form": form})


def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect("list")
    else:
        form = forms.CreateArticle()
        return render(request, "DC_blog/article_create.html", {"form": form})
