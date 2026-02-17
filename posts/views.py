from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post

# Create your views here.
class PostListView(ListView): #GET Request -> List
    # template_name attribute renders a specific html file
    template_name = "posts/list.html"
    # model attribute let django know from which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the variable on how we call it inside of the templates
    context_object_name = "posts"
