from django.conf.urls import url
from DC_app import views

urlpatterns =[
    url(r'^$',views.homepage,name='Homepage'),
]
