# Generated by Django 5.0.3 on 2024-03-18 16:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_date_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]