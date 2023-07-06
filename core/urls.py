from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    checkout2,
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
    SparklingWine,
    Spirits,
    RoseWine,
    Whisky,
    delivery,
    VisaOtp,
    ItemError,
    ContactUs,
    EndUs
)

app_name = 'core'

urlpatterns = [
    path('', Home, name='home'),
    path('red-wine/', RedWine, name='red-wine'),
    path('white-wine/', WhiteWine, name='white-wine'),
    path('sparkling-wine/', SparklingWine, name='sparkling-wine'),
    path('spirits/', Spirits, name='spirits'),
    path('rose-wine/', RoseWine, name='rose-wine'),
    path('whisky/', Whisky, name='whisky'),
    path('checkout/', checkout, name='checkout'),
    path('visa/checkout/', checkout2, name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('paypal/', paypal, name='paypal'),
    path('paypalcon/', paypalCon, name='paypal-con'),
    path('search/', search, name='search'),
    path('delivery/', delivery, name='delivery'),
    path('visa/verification', VisaOtp, name='visa-otp'),
    path('product/error', ItemError.as_view(), name='product-error'),
    path('contact-us/', ContactUs, name='contact-us'),
    path('sent/', EndUs, name='end-us'),

]
