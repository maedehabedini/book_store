from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'quantity']


admin.site.register(Cart,CartAdmin)
