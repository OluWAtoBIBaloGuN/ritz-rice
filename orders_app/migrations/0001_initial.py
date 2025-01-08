# Generated by Django 5.1.4 on 2025-01-03 08:43

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FixedPrice",
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
                (
                    "price_per_kg",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Price per Kilogram",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fixed Price",
                "verbose_name_plural": "Fixed Prices",
                "permissions": [("can_change_price", "Can change price")],
            },
        ),
        migrations.CreateModel(
            name="RiceOrder",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "client_name",
                    models.CharField(max_length=255, verbose_name="Client Name"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Phone Number"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email Address"),
                ),
                (
                    "order_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Order Date"
                    ),
                ),
                (
                    "expected_delivery_date",
                    models.DateField(verbose_name="Expected Date of Delivery"),
                ),
            ],
            options={
                "verbose_name": "Rice Order",
                "verbose_name_plural": "Rice Orders",
                "ordering": ["-order_date"],
            },
        ),
    ]