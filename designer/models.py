import json

from django.db import models

# Create your models here.


class Crossword(models.Model):
    title = models.CharField(max_length=192)
    width = models.IntegerField()
    height = models.IntegerField()


class Annotation(models.Model):
    crossword = models.ForeignKey(Crossword, on_delete=models.CASCADE, related_name='annotations')
    x = models.IntegerField()
    y = models.IntegerField()
    content = models.CharField(max_length=1024)


class Cell:
    prefix = 't'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.annotations = []
        self.content = None
