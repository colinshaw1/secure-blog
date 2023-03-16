from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #  new path for home page
    path('', includes('blog.urls')),
]
