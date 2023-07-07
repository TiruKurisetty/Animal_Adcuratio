from app.models import *
from rest_framework import serializers


# class UserForm(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['username','password','email']


class AnimalSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Animals
        fields=['name','description','images']