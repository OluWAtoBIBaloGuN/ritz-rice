# Generated by Django 5.1.4 on 2025-01-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "orders_app",
            "0010_rename_grain_type_order_grain_alter_order_amount_kg_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="ref_id",
            field=models.CharField(default=0, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("pending", "Pending"), ("completed", "Completed")],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="amount_kg",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]