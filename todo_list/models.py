from django.db import models

# Criando uma classe herdada de model
class Task(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    complete = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{str(self.id)} - {self.name}"
        
