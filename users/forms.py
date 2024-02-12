from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .import models

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email']
        labels={
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        
    def save(self, commit=True):
        our_user= super().save(commit=False)
        
        if commit==True:
            our_user.save()
            models.ProfileModel.objects.create(
                user=our_user,
                balance_amount= 10,
            )
        return our_user
        

    