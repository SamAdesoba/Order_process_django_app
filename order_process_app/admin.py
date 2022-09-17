from django.contrib import admin
from .models import Category, Customers
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name', 'description'
    ]
    list_filter = [
        'category_name', 'description'
    ]


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'company_name', 'contact_name',
    ]
