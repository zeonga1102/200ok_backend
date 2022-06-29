from tkinter import CASCADE
from django.db import models


# Create your models here.
class Dormitory(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()


class Question(models.Model):
    question = models.TextField()


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)


