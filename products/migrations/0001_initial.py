# Generated by Django 3.1.7 on 2021-04-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=20)),
                ('productPrice', models.FloatField()),
                ('sellerId', models.IntegerField()),
                ('customerId', models.IntegerField()),
            ],
            options={
                'db_table': 'Buy Products',
            },
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=20)),
                ('productPrice', models.FloatField()),
                ('sellerId', models.IntegerField()),
                ('customerId', models.IntegerField()),
            ],
            options={
                'db_table': 'Order Products',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=20)),
                ('productPrice', models.FloatField()),
                ('sellerId', models.IntegerField()),
                ('productDetails', models.TextField()),
            ],
            options={
                'db_table': 'Products Info',
            },
        ),
    ]
