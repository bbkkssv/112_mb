from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model): #OOP - Classes and Objects
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    # dunder methods or double underscor methods or magic methods in python
    def __str__(self): #or also called the "toString" method
        return f"{self.title} - {self.author}"
    
   
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])