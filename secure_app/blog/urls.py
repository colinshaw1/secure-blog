from django.urls import path
# from . import views
from .views import BlogView, DetailsPost, AddBlog, EditBlog, DeletePost, LikePost

urlpatterns = [
    # using class based views for homepage
    path('', BlogView.as_view(), name="home"),
    # using class based views to view a blog post
    path('blog/<int:pk>', DetailsPost.as_view(), name="blogpost"),
    # add blog post url
    path('add_blog/', AddBlog.as_view(), name="add_blog"),
    # add edit blog url
    path('blog/edit/<int:pk>', EditBlog.as_view(), name="edit"),
    # add delete post url
    path('blog/<int:pk>/delete', DeletePost.as_view(), name="delete"),
    # add like post url
    path('like/<int:pk>', LikePost.as_view(), name="Like"),
]