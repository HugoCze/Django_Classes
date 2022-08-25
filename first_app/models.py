from tkinter import CASCADE
from django.db import models

# Create your models here.

class User(models.Model):

    FirstName = models.CharField(max_length=64, unique=False)
    LastName = models.CharField(max_length=64, unique=False)
    Email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return  self.FirstName, self.LastName, self.Email


class Topic(models.Model):

    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
