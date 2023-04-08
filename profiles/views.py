from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
# class to register for a profile
class UserRegistration(generic.CreateView):
    template_name = 'registration/register.html'
    # once registered return to login page to login
    success_url = reverse_lazy('login')
