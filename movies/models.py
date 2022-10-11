from django.db import models
from django.contrib.auth.models import User
class moviedb(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    cast1=models.CharField(max_length=200)
    cast2=models.CharField(max_length=200)
    cast3=models.CharField(max_length=200)
    director=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class profile(models.Model):
    userp=models.OneToOneField(User,on_delete=models.CASCADE)
    title=models.ManyToManyField(moviedb)
    def __str__(self):
        return self.userp.username