from django.db import models

# Create your models here.
class Customer(models.Model):
    cname=models.CharField(max_length=15)
    custid=models.IntegerField(primary_key=True)
    address=models.TextField()
    class Meta:
        db_table='customer'
