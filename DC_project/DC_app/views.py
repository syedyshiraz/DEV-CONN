from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    return(HttpResponse("Default Page"))
def homepage(request):
    dict = {'home_page':'Welcome to the home page'}
    return(render(request, 'DC_app/homepage.html', context=dict))
