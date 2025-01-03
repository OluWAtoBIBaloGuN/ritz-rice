from django.db import models 
from django.core.validators import MinValueValidator
from django.utils.timezone import now

# Create your models here.


class FixedPrice(models.Model):
    price_per_kg = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="Price per Kilogram"
    )
    
    def __str__(self):
        return f"Price per KG: {self.price_per_kg}"

    class Meta:
        verbose_name = "Fixed Price"
        verbose_name_plural = "Fixed Prices"
        permissions = [("can_change_price", "Can change price")]

class RiceOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255, verbose_name="Client Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    order_date = models.DateField(default=now, verbose_name="Order Date")
    expected_delivery_date = models.DateField(verbose_name="Expected Date of Delivery")

    def __str__(self):
        return f"Order {self.order_id} - {self.client_name}"

    class Meta:
        verbose_name = "Rice Order"
        verbose_name_plural = "Rice Orders"
        ordering = ["-order_date"]
