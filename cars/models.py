from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    year= models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.brand}"