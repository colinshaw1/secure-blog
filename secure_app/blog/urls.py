from django.urls import path
# from . import views
from .views import BlogView

urlpatterns = [
    # using class based views for homepage
    path('', BlogView.as_view(), name="home")
]