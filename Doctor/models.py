from django.db import models

# Create your models here.
class doc(models.Model):
    fname=models.CharField(max_length=100)
    docid=models.IntegerField(default=0)
    department=models.CharField(max_length=100)
    hospital=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    
    