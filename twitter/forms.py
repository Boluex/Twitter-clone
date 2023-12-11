from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from.models import posts,comment

class update_posts(ModelForm):

    class Meta:
        model = posts
        fields = ['title','content','image']

class update_comment(ModelForm):
    class Meta:
        model = comment
        fields = ['image','content']