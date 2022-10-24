from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

WINES = (
    ('R', 'Red Wine'),
    ('W', 'White Wine'),
    ('S', 'Sparling Wine'),
    ('D', 'Dessert Wine'),
)

class Dish(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    protien = models.Charfield(max_length=50)
    paring = models.Charfield(max_length=50)

    def get_absolute_url(self):
        return reverse('dishes_detail', kwargs={'pk': self.id})

class Cheese(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    flavor = models.Charfield(max_length=100)
    description = models.TextField(max_length=250)
    dishes = models.ManyToManyField(Dish)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # changes to instance methods do not require re-generation / running of migrations
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cheese_id': self.id})

class Wine(models.Model):
    year = models.DateField('Bottle Date')
    wine = models.CharField(
        max_length=1, 
        choices=WINES, 
        default=WINES[0][0]
    )

    
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_wine_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']

# Create your models here.
 