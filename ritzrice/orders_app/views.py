from django.shortcuts import render, redirect
from django.http import HttpResponse
from orders_app.models import RiceOrder
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context = {
        'welcome_text': "Welcome to the Home page.",
    }
    return render(request, 'home.html', context)
