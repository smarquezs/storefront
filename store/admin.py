from django.contrib import admin
from django.db.models import Count
from .models import Collection, Product, Customer, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory', 'inventory_status', 'collection']
    list_editable = ['unit_price', 'inventory']
    list_per_page = 10

    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'placed_at', 'payment_status']
    list_editable = ['payment_status']
    list_per_page = 10

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_per_page = 10

    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))
