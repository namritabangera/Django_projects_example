from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=25)
    jobs=models.CharField(max_length=20)
    salary=models.FloatField()
    class Meta:
          db_table="emp_cbv"
