"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    HomepageView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("post/create", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
]
