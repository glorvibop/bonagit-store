# Generated by Django 5.1.1 on 2024-09-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_chocolateproduct_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chocolateproduct',
            old_name='name_product',
            new_name='product_name',
        ),
    ]
