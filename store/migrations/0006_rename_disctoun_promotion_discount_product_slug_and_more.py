# Generated by Django 4.0.4 on 2022-05-09 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotion',
            old_name='disctoun',
            new_name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
