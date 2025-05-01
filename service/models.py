from django.db import models

# Create your models here.
class services(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50,unique=True)
    subject=models.TextField()
    message=models.TextField()