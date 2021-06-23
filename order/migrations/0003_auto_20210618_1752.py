# Generated by Django 3.1.9 on 2021-06-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_picture'),
        ('order', '0002_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_Paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='product_orders', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_items',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
