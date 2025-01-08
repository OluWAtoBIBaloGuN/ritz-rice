# Generated by Django 5.1.4 on 2025-01-05 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders_app", "0006_delivery"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("customer_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("email_address", models.EmailField(max_length=254)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=10
                    ),
                ),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=10
                    ),
                ),
                (
                    "delivery",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders_app.delivery",
                    ),
                ),
                (
                    "grain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders_app.grain",
                    ),
                ),
            ],
        ),
    ]
