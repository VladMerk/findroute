# Generated by Django 4.1.5 on 2023-01-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Город")),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ["name"],
            },
        ),
    ]