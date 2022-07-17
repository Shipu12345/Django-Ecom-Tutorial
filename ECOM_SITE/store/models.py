from django.db import models

# Create your models here.

class Promotions(models.Model):
    descriptions=models.CharField(max_length=255)
    discount=models.FloatField()

class Collections(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Products',on_delete=models.SET_NULL,null=True,related_name='+')

class Products(models.Model):
    title = models.CharField(max_length=255)
    slug=models.SlugField(default='-')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collections,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotions)


class Customers(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )
    class Meta:
        indexes= [
            models.Index(fields=['last_name','first_name'])
        ]


class Orders(models.Model):

    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )

    customer=models.ForeignKey(Customers, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.PROTECT)
    product=models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)

class Addresses(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE
    )
    zip=models.PositiveSmallIntegerField(null=True)


class  Carts(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class CartItems(models.Model):
    cart=models.ForeignKey(Carts, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
