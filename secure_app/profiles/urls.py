from django.urls import path
from .views import UserRegistration

urlpatterns = [
    # add register view
    path('register/', UserRegistration.as_view(), name='register')
]