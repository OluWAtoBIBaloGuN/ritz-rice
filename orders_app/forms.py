from django import forms
from .models import GrainPrice
from .models import Grain
from .models import Delivery, Order
from .models import Customers
from .models import Clients




class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

# Grain type form
class GrainPriceForm(forms.ModelForm):
    class Meta:
        model = GrainPrice
        fields = ['price']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }



class GrainForm(forms.ModelForm):
    class Meta:
        model = Grain
        fields = ['name']  # Include the fields you want to display in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter grain type'}),
        }



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['location', 'price']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        }
        
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'email', 'grain', 'amount_kg']

    # You can add custom validations or widgets if necessary.
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    grain = forms.ModelChoiceField(queryset=Grain.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount_kg = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'phone_number', 'gender', 'state_of_residence']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'state_of_residence': forms.TextInput(attrs={'class': 'form-control'}),
        }   
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['organization_name', 'representative', 'email', 'phone_number', 'address', 'state', 'country']
