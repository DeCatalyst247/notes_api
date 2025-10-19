from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Note(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file= models.FileField(upload_to='uploads/',blank=True,null=True)
    def ___str__(self):
        return self.title