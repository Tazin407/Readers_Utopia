from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView, TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .import forms 

# Create your views here.
class SignUp(CreateView):
    form_class= forms.SignupForm
    template_name= 'user_signup.html'
    success_url= reverse_lazy('user_login')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['var']= 'Signup'
        return context
    
class Login(LoginView):
    template_name= 'user_signup.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['var']= 'Login'
        return context

def Logout(request):
    logout(request)
    return redirect('home')
    