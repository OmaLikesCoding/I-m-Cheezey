from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

WINES = (
    ('R', 'Red Wine'),
    ('W', 'White Wine'),
    ('S', 'Sparkling Wine'),
    ('D', 'Dessert Wine'),
)

class Dish(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    protein = models.CharField(max_length=50)
    pairing = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('dishes_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    dishes = models.ManyToManyField(Dish)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # changes to instance 
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cheese_id': self.id})

class Wine(models.Model):
    date = models.DateField('Bottle Date')
    wine = models.CharField(
        max_length=1, 
        choices=WINES, 
        default=WINES[0][0]
    )

    
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_wine_display()} on {self.date}"

  #  def __str__(self):
   #     return f"{self.get_wine_display()} on {self.date}"
    # change the default sort
    class Meta:
        ordering = ['-date']

# Create your models here.
 