from django.db import models

# Create your models here.

class QuestionPair(models.Model):
    front = models.TextField()
    back = models.TextField()
