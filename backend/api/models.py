from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") # user-obj, can do User.notes, which will give all notes created by user related-name=notes

    def __str__(self):
        return self.title
    


