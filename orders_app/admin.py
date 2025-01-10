from django.contrib import admin
from .models import Grain
from .models import GrainPrice
from .models import Order
from .models import Customers
from .models import Client, Transaction




# Register your models here.
admin.site.register(Grain) 
admin.site.register(GrainPrice)
admin.site.register(Order)
admin.site.register(Customers)
admin.site.register(Client)
admin.site.register(Transaction)

