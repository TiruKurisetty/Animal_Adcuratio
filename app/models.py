from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Animals(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    description=models.TextField()
    images=models.ImageField()
    def __str__(self):
        return self.name
        