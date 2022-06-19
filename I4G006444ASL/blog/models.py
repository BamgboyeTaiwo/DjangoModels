from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Text = models.SlugField(max_length=200, unique=True)
    Author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='posts')
    Published_date = models.DateTimeField(auto_now= True)
    Created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
