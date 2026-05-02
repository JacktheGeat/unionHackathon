from django.db import models

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Building(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField(max_length=100)
    latitude = models.FloatField(max_length=100)
    def __str__(self):
        return self.name
    
class Class(models.Model):
    classname = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.IntegerField(max_length=4)
    startTime = models.TimeField("Start Time")
    endTime = models.TimeField("End Time")
    def __str__(self):
        return self.classname

