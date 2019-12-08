from django.urls import path

from .views import (HomeView, ItemDetailView, CartView ,add_to_cart, 
remove_from_cart, OrderSummaryView, remove_single_item_from_cart, CheckoutView,
 AddCouponView, PaymentView, RequestRefundView) 

app_name = 'polls'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ItemDetailView.as_view(), name='product'),
    path('<int:pk>/cart', CartView.as_view(), name='cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('<int:item_id>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('<int:item_id>/remove-from-cart/', remove_from_cart, name='remove-from-cart'),
    path('<int:item_id>/remove-single-item-from-cart/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),    
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
        
]