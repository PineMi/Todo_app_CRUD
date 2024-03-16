from django.urls import path
from .views import touchTasks, touchTaskByID

urlpatterns = [
    path("tasks", touchTasks), #Create, Retrieve
    path("tasks/<int:task_id>", touchTaskByID), #Delete, Update, Retrieve 
]
