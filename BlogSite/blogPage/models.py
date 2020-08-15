from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #on the deletion of the user, all blogs are deleted
    body = models.TextField()

    def __str__(self):   #Lets us see the title and the author in the admin page
        return self.title + " | " + str(self.author)