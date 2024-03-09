from django.urls import path
from .views import getTasks, getTaskByID, postTask

urlpatterns = [
    path("tasks", getTasks),
    path("tasks/<int:task_id>", getTaskByID),
    path("register", postTask)


]
