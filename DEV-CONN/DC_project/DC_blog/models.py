from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='coding.png', blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:60] + "..."



class Gitpost(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    repo_name = models.CharField(max_length=100)
    repo_addr = models.URLField(max_length=2083)
    repo_desc = models.TextField(max_length=200)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.repo_name

    def snippet(self):
        return self.repo_desc[:60] + "..."
