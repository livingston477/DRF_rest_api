from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    #id=models.IntegerField(default=0, null=False)
    salary=models.IntegerField(default=0, null=False)
     
def __str__(self):
    return self.name
