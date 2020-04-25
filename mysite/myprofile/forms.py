from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']