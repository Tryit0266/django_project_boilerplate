from django.contrib import admin
from .models import Item, OrderItem, Order, Category, CardDetails, Otp, DeliveryDetails


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id',]
    prepopulated_fields = {"slug": ("name",)}

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CardDetailsAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'address', 'creditcradnum', 'expiredate', 'cvv', 'start_date',]


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CardDetails, CardDetailsAdmin)
admin.site.register(DeliveryDetails)
admin.site.register(Otp)
