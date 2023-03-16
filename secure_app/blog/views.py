from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post
# Create your views here.
# class for creating the home view
class BlogView(ListView):
    # calls the Post model 
    model = Post
    template_name = 'homepage.html'
    

class DetailsPost(DeleteView):
    model = Post
    template_name = 'blogpost.html'
