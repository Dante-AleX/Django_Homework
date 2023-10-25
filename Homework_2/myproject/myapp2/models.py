from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=254)
    reg_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    product_reg_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_summ_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)