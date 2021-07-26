from django.shortcuts import render
from django.views.generic import ListView, DetailView # new
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new
    
class DetailPageView(DetailView):
    model = Post
    template_name = 'post.html'
