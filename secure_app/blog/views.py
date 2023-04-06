from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
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
    # tell the app to use the post form
    form_class = PostForm
    template_name = 'add_blog.html'


# class to edit a blog
class EditBlog(UpdateView):
    model = Post
    template_name = "update_blog.html"
    fields = ['title', 'slug', 'body']