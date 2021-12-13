from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Firm(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name