from django.db import models

# Create your models here.
class Dish (models.Model):
    dish_name = models.CharField(max_length=255)
    def __str__(self):
        return self.dish_name
