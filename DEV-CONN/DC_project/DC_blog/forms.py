from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
        }
    ))
    content = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
        }
    ))

    class Meta:
        model = models.Blog
        fields = ["title",
                  "slug", "content",
                  'thumb']


class CreateRepo(forms.ModelForm):
    repo_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
        }
    ))
    repo_desc = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
        }
    ))

    class Meta:
        model = models.Gitpost
        fields = ["repo_name",
                  "repo_desc", "repo_addr", ]
