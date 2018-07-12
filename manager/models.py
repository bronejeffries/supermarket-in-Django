from django.db import models

# Create your models here.
class Employee(models.Model):
    First_Name =  models.CharField(max_length = 50)
    Last_Name =  models.CharField(max_length = 50)
    Address =  models.CharField(max_length = 45)
    Contact= models.CharField(max_length = 14)
    Country= models.CharField(max_length = 25)
    Salary = models.CharField(max_length = 8)

    def __str__(self):
        return self.First_Name +' '+ self.Last_Name

# class Cashier(Employee):
#     password =  models.CharField(max_length = 250)
#     username = models.CharField(max_length = 250)

class Tasks(models.Model):
    Task =  models.CharField(max_length = 250)

    def __str__(self):
        return self.Task
