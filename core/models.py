from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime


LABEL_CHOICES = (
    ('p', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),

)


class Category (models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product-category", kwargs={"slug": self.slug})


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES,
                             max_length=20, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total


class CardDetails(models.Model):
    fullname = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    creditcradnum = models.CharField( max_length=19)
    expiredate = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    start_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.fullname

class DeliveryDetails(models.Model):
    fullname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    address = models.CharField( max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


class Otp(models.Model):
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.otp