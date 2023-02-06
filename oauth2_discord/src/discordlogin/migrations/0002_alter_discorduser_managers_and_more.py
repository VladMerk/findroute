# Generated by Django 4.1.6 on 2023-02-06 18:54

import discordlogin.managers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discordlogin", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="discorduser",
            managers=[
                ("objects", discordlogin.managers.DiscordUserOAuth2Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="discorduser",
            name="last_login",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
