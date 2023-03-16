from django.urls import path
# from . import views
from .views import BlogView, DetailsPost

urlpatterns = [
    # using class based views for homepage
    path('', BlogView.as_view(), name="home"),
     # using class based views for homepage
    path('blog/<int:pk>', DetailsPost.as_view(), name="blogpost"),
]