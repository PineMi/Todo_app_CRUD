from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task
from .serializer import TaskReadSerializer, TaskWriteSerializer


#Retrieve or Create
@api_view(["GET", "POST"])
def touchTasks(request):
    if request.method == "GET":
        print("Client Retrieved Tasks data...")
        tasks = Task.objects.all()    
        serializer = TaskReadSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print("Client Posted a new tasks data...")
        data = request.data
        serializer = TaskWriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# Delete, Update, Retrieve 
@api_view(["DELETE", "PATCH", "GET"])
def touchTaskByID(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        print("Client Deleted a task data...")
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PATCH":
        print("Client updated a task data...")

        serializer = TaskWriteSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        print("Client retrieved a task data...")

        serializer = TaskReadSerializer(task)
        return Response(serializer.data)
     
#TODO: Replicate in a Class Based View