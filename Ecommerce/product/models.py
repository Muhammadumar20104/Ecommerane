from django.db import models
class Customer(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_No = models.IntegerField(max_length=11)
# Create your models here.
