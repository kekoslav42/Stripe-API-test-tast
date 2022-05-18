from django.urls import path

from . import views

urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item),
    path('item/<int:item_id>/', views.item),
    path('order/<int:order_id>', views.order),
    path('order/new/', views.create_order),
    path('order/<int:order_id>/add/<int:item_id>', views.add_item_to_order),
    path('order/<int:order_id>/buy', views.buy_order)
]