from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post
# Create your views here.
# class for creating the home view
class BlogView(ListView):
    # calls the Post model 
    model = Post
    template_name = 'homepage.html'
    
# view to view a blog post details
class DetailsPost(DeleteView):
    model = Post
    template_name = 'blogpost.html'

# class to add a blog post
class AddBlog(CreateView):
    model = Post
    template_name = 'add_blog.html'
    fields = '__all__'