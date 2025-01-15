from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path('', views.teams_list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit_team, name='edit'),
    path('<int:pk>/activate/', views.teams_activate, name='activate'),
    path('select-team-plan/', views.select_team_plan, name='select_team_plan'),
    path('payment/', views.payment, name='payment'),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
]