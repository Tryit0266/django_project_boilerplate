from django.contrib import admin
from .models import Item, OrderItem, Order, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id',]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category, CategoryAdmin)
