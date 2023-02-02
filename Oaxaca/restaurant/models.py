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
    dish_availability = models.BooleanField=()

    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return self.dish_name

class Customer(models.Model):
    table_id = models.AutoField(primary_key = True)
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    persons = models.IntegerField(max_digits = 10)
    need_help = models.BooleanField(default = False)

    def __str__(self):
        return self.table_id

class Status(models.Model):
    StatusChoices = [
        (InProgress, 'Order in progress')
        (Received, 'Received'),
        (Cooking, 'Cooking'),
        (Problem, 'Problem'),
    ]
    status_id = models.AutoField(primary_key = True)
    status_name = models.CharField(max_length = 2, choices=StatusChoices, default=InProgress)

    def __str__(self):
        return self.status_name

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_time = models.DateTimeField()
    table_id = models.ForeignKey(Customer)
    order_finish = models.BooleanField(Default = False)
    dish_id = models.ManyToManyField(Dish)
    status_id = models.ForeignKey(Stauts)

    def __str__(self):
        return "Order no: " + self.order_id