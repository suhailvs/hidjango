from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    # created_by = models.IntegerField(null=True)
    created_by = models.ForeignKey('User', 
        on_delete= models.CASCADE, 
        related_name='%(app_label)s_%(class)s_created_by', null=True) #
    updated_by = models.IntegerField(null=True)

    class Meta:
        abstract = True


class User(AbstractUser,BaseModel):
    # Added fields
    USER_TYPE_CHOICES = (
        ('SU', 'Super User'),
        ('A', 'Admin'),
        ('PR','Principal'),
        ('T', 'Teacher'),
        ('E', 'Employee'),
        ('S', 'Student'),
        ('P', 'Parent'),
        ('MN','Manager'),
        ('AN', 'Anonymous'),
    )
    
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(default = 1)

from django.conf import settings

# https://stackoverflow.com/questions/38556217/
class Nugget(BaseModel):
    added_by = models.IntegerField(null=True) # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='added_by', blank=True, null=True)

from rest_framework import serializers
class NuggetSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = Nugget
        fields = "__all__"
