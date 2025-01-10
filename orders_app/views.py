from django.shortcuts import render, redirect, get_object_or_404  # Ensure get_object_or_404 is imported
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import LoginForm, DeliveryForm
from .models import Grain, GrainPrice, Delivery, Client
from .forms import GrainForm, OrderForm, Order, CustomerForm, ClientForm, TransactionForm
from django.db.models import Count
from .models import Customers, Order, Transaction


# Create your views here.

def grain_view(request):
    # Get all grain types
    grains = Grain.objects.all()
    
    # Handle the form submission
    if request.method == 'POST':
        form = GrainForm(request.POST)
        if form.is_valid():
            form.save()  # Save the grain type to the database
            return redirect('grain')  # Redirect to the grain page after form submission
    else:
        form = GrainForm()

    # Pass both the form and the list of grains to the template
    return render(request, 'grain.html', {'form': form, 'grains': grains})




def home(request):
    context = {
        'welcome_text': "Welcome to the Home page.",
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'welcome_text': "About -Ritz Rice",
        'details': 'Email: akpojarohrita@gmail.com<br>Contact: 949b Dipo Oshikoya street, Omole 2, Lagos.<br>telephone:+234 806 743 3077'

    }
    return render(request, 'about.html', context)


def admin(request):
    context = {
        'welcome_text': "Admin -Ritz Rice",
    }
    return render(request, 'admin.html', context)

def order(request):
    context = {
        'welcome_text': "Orders -Ritz Rice",
    }
    return render(request, 'orders.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('authenticated')  # Redirect to the home page or dashboard
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'admin.html', {'form': form})

def authenticated(request):
    context = {
        'welcome_text': "Welcome",
    }
    return render(request, 'authenticated.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')  

def prices_view(request):
    # Automatically create GrainPrice objects for any missing grains
    for grain in Grain.objects.all():
        GrainPrice.objects.get_or_create(grain=grain, defaults={'price': 0.00})

    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        new_price = request.POST.get('price')
        try:
            grain_price = GrainPrice.objects.get(id=form_id)
            grain_price.price = new_price
            grain_price.save()
        except GrainPrice.DoesNotExist:
            pass
        return redirect('prices')  # Reload the page after updating the price

    grain_prices = GrainPrice.objects.all()
    return render(request, 'prices.html', {'grain_prices': grain_prices})



def delivery_view(request):
    if request.method == 'POST':
        # Handle price updates
        if 'delivery_id' in request.POST:
            delivery_id = request.POST.get('delivery_id')
            price = request.POST.get('price')
            try:
                delivery = Delivery.objects.get(id=delivery_id)
                delivery.price = price
                delivery.save()
                return redirect('delivery')
            except Delivery.DoesNotExist:
                pass
        else:
            # Handle adding new delivery locations
            form = DeliveryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('delivery')

    # For GET requests, display the form and existing data
    form = DeliveryForm()
    deliveries = Delivery.objects.all()
    return render(request, 'delivery.html', {'form': form, 'deliveries': deliveries})





def grain_and_delivery_view(request):
    # Fetch all GrainPrice and Delivery data
    grain_prices = GrainPrice.objects.select_related('grain').all()
    deliveries = Delivery.objects.all()

    # Render to the template
    return render(request, 'orders/grain_and_delivery.html', {
        'grain_prices': grain_prices,
        'deliveries': deliveries,
    })
    

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the order data to the database
            return redirect('home')  # Redirect to the home page after order is saved
    else:
        form = OrderForm()  # If GET request, just show the empty form

    return render(request, 'orders_app/order.html', {'form': form})
        

def customer_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page (make sure 'success' is a valid URL name)
    else:
        form = CustomerForm()

    return render(request, 'customers.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')



def order_list_view(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)  # Use get_object_or_404 to fetch the order
        order.status = 'completed'
        order.save()
        return HttpResponseRedirect('/home/orders/')  # Redirect to the same page after updating the order

    orders = Order.objects.all()  # Fetch all orders
    return render(request, 'orderlist.html', {'orders': orders})

def order_detail_view(request, ref_id):
    order = get_object_or_404(Order, ref_id=ref_id)
    return render(request, 'order_detail.html', {'order': order})


def clients(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Ensure 'success' URL is defined in your `urls.py`
    else:
        form = ClientForm()

    return render(request, 'clients.html', {'form': form})
 

def record_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        form = TransactionForm()
    
    return render(request, 'transactions.html', {'form': form})              



def statistics_view(request):
    # Pie chart: Gender demographics from Customers model
    gender_data = Customers.objects.values('gender').annotate(count=Count('id'))
    gender_labels = [item['gender'] for item in gender_data]
    gender_counts = [item['count'] for item in gender_data]

    # Bar chart: State of origin from Customers model
    state_data = Customers.objects.values('state_of_residence').annotate(count=Count('id'))
    state_labels = [item['state_of_residence'] for item in state_data]
    state_counts = [item['count'] for item in state_data]

    # Bar chart: Type of grain bought from Orders model
    grain_data = Order.objects.values('grain__name').annotate(count=Count('id'))
    grain_labels = [item['grain__name'] for item in grain_data]
    grain_counts = [item['count'] for item in grain_data]

    # Bar chart: Count of business done by transacting org from Transactions model
    org_data = Transaction.objects.values('transacting_org__organization_name').annotate(count=Count('id'))
    org_labels = [item['transacting_org__organization_name'] for item in org_data]
    org_counts = [item['count'] for item in org_data]

    context = {
        'gender_labels': gender_labels,
        'gender_counts': gender_counts,
        'state_labels': state_labels,
        'state_counts': state_counts,
        'grain_labels': grain_labels,
        'grain_counts': grain_counts,
        'org_labels': org_labels,
        'org_counts': org_counts,
    }
    return render(request, 'statistics.html', context)


