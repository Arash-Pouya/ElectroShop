# Generated by Django 3.1.9 on 2021-06-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]