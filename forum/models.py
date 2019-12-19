from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.TextField()
    description = models.TextField()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    
