# Generated by Django 5.1.2 on 2024-10-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ninja_apikey", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="hashed_key",
            field=models.CharField(max_length=128),
        ),
    ]