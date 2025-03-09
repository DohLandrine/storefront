from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 255),
    description = models.TextField(),
    # Always use DecimalField for monetry values.
    # From below, a number with 6 digits and  2 decimal place is 9999.99
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField(),
    last_update = models.DateTimeField(auto_now = True)

class Customer(models.Model):
    first_name = models.CharField(max_length = 255),
    last_name = models.CharField(max_length = 255),
    email = models.EmailField(unique = True),
    phone = models.CharField(max_length = 255),
    birth_date = models.DateField(null = True),


