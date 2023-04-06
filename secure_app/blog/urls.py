from django.urls import path
# from . import views
from .views import BlogView, DetailsPost, AddBlog, EditBlog

urlpatterns = [
    # using class based views for homepage
    path('', BlogView.as_view(), name="home"),
    # using class based views to view a blog post
    path('blog/<int:pk>', DetailsPost.as_view(), name="blogpost"),
    # add blog post url
    path('add_blog/', AddBlog.as_view(), name="add_blog"),
    # add edit blog url
    path('blog/edit/<int:pk>', EditBlog.as_view(), name="edit"),
]