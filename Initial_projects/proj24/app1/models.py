from django.db import models

# Create your models here.
class Library(models.Model):
    name= models.CharField(max_length=25)
    location=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=50)    
    author=models.CharField(max_length=50)
    library=models.ForeignKey(Library,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
    