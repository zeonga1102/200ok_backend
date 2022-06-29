from django.db import models


class Board(models.Model):
    content = models.CharField(max_length=250)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)