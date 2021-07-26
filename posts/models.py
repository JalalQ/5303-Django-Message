from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default="No Title")
    text = models.TextField()
    #name = models.CharField(max_length=50, verbose_name="Name", null=True)
    date_created = models.DateField(verbose_name="Date of Message", auto_now_add=True)
    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:50] + "... by " + self.author.first_name
    
    #use the get_absolute_url() method in your templates to link to specific posts.
    #https://docs.djangoproject.com/en/3.2/ref/models/instances/#get-absolute-url
    def get_absolute_url(self):
        return "../messages/post/%i/" % self.id
        
