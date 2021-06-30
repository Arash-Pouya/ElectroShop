# Generated by Django 3.1.9 on 2021-06-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_category_name_persian'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default='hp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='laptop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='hp_db1100ny'),
            preserve_default=False,
        ),
    ]