from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25)
    dept=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class EmpIdCard(models.Model):
      emp=models.OneToOneField(Employee,on_delete=models.CASCADE)
      card_number=models.CharField(max_length=20,unique=True)
      issue_date=models.DateField(auto_now_add=True)
      def __str__(self):
           return f"{self.emp.name}'s ID:{self.card_number}"
