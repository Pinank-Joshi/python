from django.db import models

# Create your models here.
class userinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    age=models.IntegerField()
