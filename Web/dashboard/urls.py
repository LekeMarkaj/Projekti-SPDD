
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
]