from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.title

class D(models.Model):
    tit = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    ques = models.CharField(max_length=30)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    def __str__(self):
        return str(self.tit)