# Generated by Django 3.1.7 on 2021-04-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_customerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customerToken',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]