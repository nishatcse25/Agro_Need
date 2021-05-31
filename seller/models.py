from django.db import models

# Create your models here.

class Seller(models.Model):
    sellerName = models.CharField(max_length=20)
    sellerEmail = models.EmailField(max_length=50)
    sellerContact = models.CharField(max_length=11)
    sellerPassword = models.CharField(max_length=20)
    sellerToken = models.CharField(max_length=4,default='0000')
    sellerImage = models.ImageField(upload_to='seller_img/images',default='default.png')

    class Meta:
        db_table = 'Seller Info'


class TemporaryS(models.Model):
    sellerName = models.CharField(max_length=20)
    sellerPassword = models.CharField(max_length=20)

    class Meta:
        db_table = 'Seller Temporary Data'