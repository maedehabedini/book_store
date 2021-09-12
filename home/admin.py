from django.contrib import admin
from .models import Category, Book


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'created', 'update', 'inventory', 'available', 'unit_price', 'percent_discount',
        'cash_discount',
        'total_price')
    list_filter = ('available',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
