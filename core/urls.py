from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    Home,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    paypal,
    paypalCon,
    search,
    RedWine,
    WhiteWine,
    delivery,
    VisaOtp,
    ItemError
)

app_name = 'core'

urlpatterns = [
    path('', Home, name='home'),
    path('red-wine/', RedWine, name='red-wine'),
    path('white-wine/', WhiteWine, name='white-wine'),
    path('checkout/', checkout.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('paypal/', paypal, name='paypal'),
    path('paypalcon/', paypalCon, name='paypal-con'),
    path('search/', search, name='search'),
    path('delivery/', delivery.as_view(), name='delivery'),
    path('visa/verification', VisaOtp, name='visa-otp'),
    path('product/error', ItemError.as_view(), name='product-error'),
]
