from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostQuestion(models.Model):
    question=models.TextField(null=True, blank=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(blank=True,null=True)
    

class Answer(models.Model):
    answer=models.TextField(null=True, blank=True)
    question=models.ForeignKey(PostQuestion,on_delete=models.CASCADE)
    answer_by=models.CharField(max_length=50,null=True,blank=True)
    liked=models.BooleanField(default=False)
    created_at=models.DateTimeField(blank=True,null=True)