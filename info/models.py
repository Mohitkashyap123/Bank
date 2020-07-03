from django.db import models

# Create your models here.

#from django.db.models import Model


class Bank(models.Model):
    ifsc = models.CharField(max_length=25)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name