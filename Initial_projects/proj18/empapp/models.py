from django.db import models

# Create your models here.

class EmpModel(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    empjob=models.CharField(max_length=15)
    empsal=models.FloatField()
    class Meta:
        db_table='emp'

