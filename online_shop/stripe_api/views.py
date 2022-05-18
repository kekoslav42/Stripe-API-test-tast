import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Item, Order

stripe.api_key = settings.STRIPE_API_KEY


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(
        request,
        'order.html',
        {'item': item}
    )


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://github.com/kekoslav42',
        cancel_url='https://github.com/kekoslav42',
    )
    return JsonResponse({'session_id': session.id})


def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(
        request,
        'order_list.html',
        {'order': order}
    )


def create_order(request):
    order = Order.objects.create()
    return JsonResponse({'order_id': order.id})


def add_item_to_order(request, order_id, item_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.item.filter(pk=item_id).exists():
        return JsonResponse({'Error': 'The item has already been added'})
    item = get_object_or_404(Item, pk=item_id)
    order.item.add(item)
    order.total_sum += item.price
    order.save()
    return JsonResponse({'Success': 'Item add to order'})


def buy_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = []
    for item in order.item.all():
        items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.name
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        })
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='https://github.com/kekoslav42',
        cancel_url='https://github.com/kekoslav42',
    )
    return JsonResponse({'session_id': session.id})
