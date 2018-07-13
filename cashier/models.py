from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 250)
    selling_price = models.IntegerField()
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Sales(models.Model):
    product_in_sales = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    date_of_sale = models.DateField(auto_now_add=True)
    total_amount = models.IntegerField()



class Purchases(models.Model):
    product_in_purchases = models.ForeignKey(Products, on_delete=models.CASCADE)
    Cost_price = models.IntegerField()
    quantity_purchased = models.IntegerField()
    date_of_purchase = models.DateField(auto_now_add=True)
    total = models.IntegerField(default=0)

# class Expenses(models.Model):
