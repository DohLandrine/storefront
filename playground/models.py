from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length = 255),

class Product(models.Model):
    title = models.CharField(max_length = 255),
    description = models.TextField(),
    # Always use DecimalField for monetry values.
    # From below, a number with 6 digits and  2 decimal place is 9999.99
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField(),
    last_update = models.DateTimeField(auto_now = True),
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)

class Customer(models.Model):
    first_name = models.CharField(max_length = 255),
    last_name = models.CharField(max_length = 255),
    email = models.EmailField(unique = True),
    phone = models.CharField(max_length = 255),
    birth_date = models.DateField(null = True),

    # Choice Field
    membership_bronze = 'B'
    membership_silver = 'S'
    membership_gold = 'G'
    MEMBERSHIP_CHOICES = [
        (membership_bronze, 'bronze')
        (membership_silver, 'silver')
        (membership_gold, 'gold')
    ]
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = membership_bronze)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add = True),
    # Choice Field
    payment_status_pending = 'P'
    payment_status_complete = 'C'
    payment_status_failed = 'F'
    PAYMENT_STATUS_CHOICES = [
        (payment_status_pending, 'pending'),
        (payment_status_failed, 'failed'),
        (payment_status_complete, 'complete')
    ]
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = payment_status_pending),
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)

class Address(models.Model):
    city = models.CharField(max_length = 255),
    street = models.CharField(max_length = 255),
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key = True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True),

class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField(),
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE),
    product = models.ForeignKey(Product, on_delete = models.CASCADE),
    quantity = models.PositiveSmallIntegerField()