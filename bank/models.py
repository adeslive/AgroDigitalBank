from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length = 200)

class Client(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    date_of_birth = models.DateField()
    dni = models.CharField(max_length=13)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)