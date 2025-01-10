from django.urls import path
from orders_app import views


urlpatterns = [
    path('grain/', views.grain_view, name='grain'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('admin', views.admin, name='admin'),
    path('orders', views.order, name='order'),
    path('admin/', views.login_view, name='admin'),
    path('authenticated/', views.authenticated, name='authenticated'),
    path('logout/', views.logout_view, name='logout'),
    path('prices/', views.prices_view, name='prices'),
    path('delivery/', views.delivery_view, name='delivery'),
    path('pricelist/', views.grain_and_delivery_view, name='pricelist'),
    path('order/', views.order_view, name='order'),
    path('customers/', views.customer_view, name='customers'),
    path('orders/', views.order_list_view, name='orderlist'),
    path('clients/', views.clients, name='clients'),
    path('order/<str:ref_id>/', views.order_detail_view, name='order_detail'),
    path('success/', views.success_view, name='success'),
    path('clients/', views.clients, name='clients'),
    path('transactions/', views.record_transaction, name='transactions'),
    path('statistics/', views.statistics_view, name='statistics'),
    
    
    
    
]