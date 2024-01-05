import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    DoesnotExist = None
    objects = None
    question_text = models.CharField(max_length=200)
    pub_text = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    boolean = True,
    ordering = 'pub_text',
    description = 'Published recently?',

    def was_published_recently(self):
        pass


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_text <= now


class Choice(models.Model):
    DoesNotExist = None
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
