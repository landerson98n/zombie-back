from django.db import models

class Survivor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    infected = models.PositiveIntegerField(default=0)
    is_infected = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(max_length=200)
    survivor = models.ForeignKey(Survivor, related_name='items',on_delete=models.CASCADE)
