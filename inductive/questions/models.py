from django.db import models

# Create your models here.

class Chapter(models.Model):
    book = models.CharField(max_length=20)
    chap = models.IntegerField(default=1)
    def __str__(self):
        return "%s:%d" %(self.book, self.chap)

class Question(models.Model):
    reference = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='points_to')
    question_text = models.TextField(max_length=400)