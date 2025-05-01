from django.db import models

# Create your models here.
class output(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    year = models.IntegerField()
    branch = models.CharField(max_length=15)
    start_destination = models.CharField(max_length=25)
    end_destination = models.CharField(max_length=25)
    submit_time = models.DateTimeField(auto_now_add=True)