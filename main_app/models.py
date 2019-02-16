from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    text = models.TextField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class MedicalExpert(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    clients = models.ManyToManyField(User)
