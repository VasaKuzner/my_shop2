# Generated by Django 4.2.3 on 2023-11-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_city_remove_order_city_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phonenumb',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]