from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task
from .serializer import TaskReadSerializer, TaskWriteSerializer


# Get all Tasks
@api_view(["GET"])
def getTasks(request):
    tasks = Task.objects.all()    
    serializer = TaskReadSerializer(tasks, many=True)

    return Response(serializer.data)

# Get a specific Task
@api_view(["GET"])
def getTaskByID(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
     
    serializer = TaskReadSerializer(task)
    return Response(serializer.data)


# Post a New Task
@api_view(["POST"])
def postTask(request):
    # Assuming you are sending task data in the request body
    data = request.data
    serializer = TaskWriteSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)