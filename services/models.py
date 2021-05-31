from django.db import models

# Create your models here.

class Services(models.Model):
    servicesName = models.CharField(max_length=20)
    servicesPrice = models.FloatField()
    sellerId = models.IntegerField()
    serviceDetails = models.TextField()

    class Meta:
        db_table = 'Service Info'


class RentServices(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.FloatField()
    sellerId = models.IntegerField()
    customerId = models.IntegerField()

    class Meta:
        db_table = 'Rent Services'
