# Generated by Django 4.1.7 on 2023-03-04 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_products_productss'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productss',
            new_name='NewProducts',
        ),
    ]
