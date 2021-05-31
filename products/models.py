from django.db import models

class Products(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.FloatField()
    sellerId = models.IntegerField()
    productDetails = models.TextField()
    @staticmethod
    def getAllProducts():
        return Products.objects.all()

    class Meta:
        db_table = 'Products Info'


class OrderProducts(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.FloatField()
    sellerId = models.IntegerField()
    customerId = models.IntegerField()

    class Meta:
        db_table = 'Order Products'


class BuyProducts(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.FloatField()
    sellerId = models.IntegerField()
    customerId = models.IntegerField()

    class Meta:
        db_table = 'Buy Products'