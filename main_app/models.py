from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()


class JournalEntry(models.Model):
    text = models.TextField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class MedicalExpert(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    clients = models.ManyToManyField(User)
