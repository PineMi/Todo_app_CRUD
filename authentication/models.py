from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='pfp/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} -> {self.user.email}'
