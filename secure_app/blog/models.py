from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name='blog')
    # defining delf string to return the 
    # title of the blog and blooger name
    def __str__(self):
        return self.title + '|' + str(self.blogger)

    # add absoulte url function so that post can return to the blogpost page
    def get_absolute_url(self):
        return reverse('home')