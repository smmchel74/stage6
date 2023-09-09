import bank_sber

from django.shortcuts import render, redirect, reverse, get_object_or_404
from decimal import Decimal
from django.conf import settings
from orders.models import Order

# Create your views here.
bank_sber.api_key = settings.BANK_SECRET_KEY
bank_sber.api_version = settings.BANK_API_VERSION


def payment_process(request):
    order_id = request.session.get(
        'order_id',
        None
    )
    order = get_object_or_404(
        Order,
        id=order_id
    )
    if request.method == 'POST':
        success_url = request.build_absolute_uri(
            reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(
            reverse('payment:canceled'))
        # данные сеанса оформления платежа SBER
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # создать сеанс оформления платежа SBER
        session = bank_sber.checkout.Session.create(**session_data)
        # перенаправить к платежной форме SBER
        return redirect(session.url, code=303)
    else:
        return render(
            request,
            'payment/process.html',
            locals()
        )