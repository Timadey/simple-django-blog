from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here
class HomepageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "post_create.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_edit.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
