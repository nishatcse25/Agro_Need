from django.db import models

# Create your models here.

class Customer(models.Model):
    customerName = models.CharField(max_length=20)
    customerEmail = models.EmailField(max_length=50)
    customerContact = models.CharField(max_length=11)
    customerToken = models.CharField(max_length=4)
    customerPassword = models.CharField(max_length=20)
    customerImage = models.ImageField(default='default.png', upload_to='customer_img/images')

    class Meta:
        db_table = 'Customer Info'

class TemporaryC(models.Model):
    customerName = models.CharField(max_length=20)
    customerPassword = models.CharField(max_length=20)

    class Meta:
        db_table = 'Customer Temporary Data'