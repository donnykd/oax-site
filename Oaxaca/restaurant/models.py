from django.db import models

# Create your models here.

class Allergies(models.Model):
    allergies_id = models.AutoField(primary_key = True)
    allergies_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.allergies_name

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key = True)
    allergies_id = models.ManyToManyField(Allergies)
    ingredient_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.ingredient_name

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.category_name

class Dish(models.Model):
    dish_id = models.AutoField(primary_key = True)
    dish_name = models.CharField(max_length = 75)
    dish_quantity = models.IntegerField(max_digits=3)
    dish_price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_calories = models.IntegerField()
    dish_availability = models.BooleanField=(default=False)

    category_id = models.ManyToManyField(Category)

    def __str(self):
        return self.dish_name
