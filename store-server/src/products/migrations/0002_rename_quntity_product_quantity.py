# Generated by Django 4.1.5 on 2023-01-29 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quntity",
            new_name="quantity",
        ),
    ]