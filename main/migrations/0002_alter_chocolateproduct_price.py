# Generated by Django 5.1.1 on 2024-11-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolateproduct',
            name='price',
            field=models.IntegerField(),
        ),
    ]
