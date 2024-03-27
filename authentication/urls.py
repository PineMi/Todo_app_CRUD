from django.urls import path
from .views import register, login

urlpatterns = [
    path("register", register), # Create
    path("login", login) # Post
]
