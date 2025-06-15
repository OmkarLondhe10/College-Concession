from django.db import models

# Create your models here.
class Concession(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    roll=models.IntegerField()
    year=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    start_dest=models.CharField(max_length=50)
    end_dest=models.CharField(max_length=30)
    period=models.CharField(max_length=20)