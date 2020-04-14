from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumb = models.ImageField(default='default.png',blank=True)
    # author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Gitpost(models.Model):
    repo_name  = models.CharField(max_length=100)
    repo_addr = models.URLField(max_length=200)
    repo_desc = models.TextField()
    # author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)


    def __str__(self):
        return self.repo_name
