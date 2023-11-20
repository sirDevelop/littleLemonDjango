from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class DeliveryCrew(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username