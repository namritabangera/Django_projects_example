from django.db import models

# Create your models here.
class StudentModel(models.Model):
    rollno=models.IntegerField()
    sname=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    fees=models.FloatField()
    
