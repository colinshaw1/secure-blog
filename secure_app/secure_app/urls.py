from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #  new path for home page
    path('', include('blog.urls')),
    # add profiles url
    path('profiles/', include('django.contrib.auth.urls')),
]
