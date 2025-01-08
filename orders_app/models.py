from django.db import models 
from django.core.validators import MinValueValidator
from django.utils.timezone import now
import random
import string


# Create your models here.
class Grain(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GrainPrice(models.Model):
    grain = models.OneToOneField(Grain, on_delete=models.CASCADE)  # Ensure each grain has one price
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default price to 0.00

    def __str__(self):
        return f"{self.grain.name} - {self.price}"
    
    
class Delivery(models.Model):
    location = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.location} - ₦{self.price}"
    
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    ref_id = models.CharField(max_length=15, unique=True, blank=False)  # Unique reference ID
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    grain = models.ForeignKey('Grain', on_delete=models.CASCADE)  # Assuming 'Grain' model exists
    amount_kg = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateField(default=now)  # Automatically sets the current date
    expected_delivery_date = models.DateField(default="2025-01-15")  # Default delivery date

    def __str__(self):
        return f"Order by {self.name} for {self.grain.name}"

    def save(self, *args, **kwargs):  # Corrected to use *args
        if not self.ref_id:  # Generate ref_id if not already set
            self.ref_id = ''.join(random.choices(string.digits, k=10))
        super().save(*args, **kwargs)


    

class Customers(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, help_text="Preferably a WhatsApp number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    state_of_residence = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Clients(models.Model):
    organization_name = models.CharField(max_length=255)
    representative = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Nigeria')

    def __str__(self):
        return self.organization_name


