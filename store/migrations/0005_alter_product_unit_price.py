# Generated by Django 4.0.4 on 2022-05-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_slug_alter_product_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
