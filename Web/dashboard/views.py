import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from django.http import JsonResponse

from lead.models import lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    team = request.user.userprofile.get_active_team()
    
    leads = lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })

def make_payment(request):
    if request.method == "POST":
        try:
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=5000,  # Amount in cents ($50.00)
                currency="usd",
                automatic_payment_methods={"enabled": True},
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'dashboard/make_payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def payment_success(request):
    return render(request, 'dashboard/payment_success.html')
