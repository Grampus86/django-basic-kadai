# Generated by Django 4.2.1 on 2024-03-31 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
