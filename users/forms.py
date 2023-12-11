from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from.models import profile

class renew(ModelForm):
    email= forms.EmailField()
    name = forms.CharField(max_length=2000)
    class Meta:
        model = User
        fields = ['username','name','email']

class person(ModelForm):
    class Meta:
        model = profile
        fields = ['image']