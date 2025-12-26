from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=25)
    empjob=models.CharField(max_length=25)
    empsal=models.FloatField()