from django.urls import path
from orders_app import views

urlpatterns = [
    path('', views.home, name='home'),
]