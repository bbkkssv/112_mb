from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.
class PostListView(ListView): #GET Request -> List
    # template_name attribute renders a specific html file
    template_name = "posts/list.html"
    # model attribute let django know from which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the variable on how we call it inside of the templates
    context_object_name = "posts"

    # ListView is the same as SELECT * FROM posts_post; in SQL
    # DetailsView is the same as SELECT * FROM posts_post WHERE id = 1; in SQL

class PostDetailView(DetailView): #GET Request -> Detail
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): # POST Request -> form (HTML)
    template_name = "posts/new.html"
    model = Post
    # fields attribute is a list that allow us to enable/disable the inputs to render in the html
    fields = ["title","subtitle","body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView): # POST Request -> form (HTML)
    template_name = "posts/edit.html"
    model = Post
    fields = ["title","subtitle","body"]


class PostDeleteView(DeleteView): # POST Request -> form (HTML)
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("posts:post_list")
