from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^link_repo/$', views.link_repo, name="link"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),

]
