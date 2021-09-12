from django.shortcuts import render

from .models import (Category,
                     Book,
                     )
from .forms import SearchForm
from django.db.models import Q
from cart.models import CartForm

def home(request):
    category = Category.objects.all()
    return render(request, 'home/home.html', {'category': category})


def all_product(request, id=None):
    books = Book.objects.all()
    form = SearchForm(request.POST)
    category = Category.objects.all()
    if 'search' in request.GET:  # اگر چیزی که کاربز سرچ کرد داخل متد گت بود:
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            books = books.filter(title__exact=data)
    if id:
        data = Category.objects.get(id=id)
        books = books.filter(category=data)
    return render(request, 'home/product.html', {'books': books, 'category': category, 'form': form})


def product_detail(request, id):
    cart_form = CartForm
    book = Book.objects.get(id=id)
    return render(request, 'home/detail.html', {'book': book,'cart_form':cart_form})


def product_search(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']  # همون فیلدی که توی فرم هست رو باید بگیره
            if data is not None:
                books = books.filter(
                    Q(percent_discount__exact=data) | Q(unit_price__exact=data))  # میتونه بر اساس تخفیف یا قیمت سرچ کنه

            else:
                books = books.filter(title__exact=data)  # براساس اسم کتاب

            return render(request, 'home/product.html', {'books': books, 'form': form})
