from django.db import models

# Create your models here.

class Chapter(models.Model):
    book = models.CharField(max_length=20)
    chapter = models.IntegerField()

class Question(models.Model):
    reference = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
    )
    question_text = models.CharField(max_length=400)