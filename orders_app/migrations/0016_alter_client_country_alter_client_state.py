# Generated by Django 5.1.4 on 2025-01-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders_app", "0015_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="country",
            field=models.CharField(default="Nigeria", max_length=100),
        ),
        migrations.AlterField(
            model_name="client",
            name="state",
            field=models.CharField(max_length=100),
        ),
    ]
