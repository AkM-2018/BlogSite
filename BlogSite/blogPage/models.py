from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):   #Lets us see the title and the author in the admin page
        return self.name

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #on the deletion of the user, all blogs are deleted
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):   #Lets us see the title and the author in the admin page
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))
        #return reverse('home')
