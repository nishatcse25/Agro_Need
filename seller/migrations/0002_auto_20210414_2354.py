# Generated by Django 3.1.7 on 2021-04-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='rating',
        ),
        migrations.AddField(
            model_name='seller',
            name='sellerImage',
            field=models.ImageField(default='default.png', upload_to='seller_img/images'),
        ),
    ]
