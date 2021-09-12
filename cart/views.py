from django.shortcuts import render, redirect
from home.models import Book
from .models import *


def cart_detail(request):
    total = 0
    cart = Cart.objects.filter(user_id=request.user.id)
    for b in cart:
        total += b.book.total_price * b.quantity
    return render(request, 'cart/cart.html', {'cart': cart, 'total': total})


def add_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    book = Book.objects.get(id=id)  # اول باید ببینیم کدوم محصوله
    data = Cart.objects.filter(user_id=request.user.id, book_id=id)  # چک بشه که آیا سفارش توی سبد خرید وجود داشته؟
    if data:
        check = 'yes'
    else:
        check = 'no'
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'yes':
                shop = Cart.objects.get(user_id=request.user.id, book_id=id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(user_id=request.user.id, book_id=id, quantity=info)
        return redirect(url)  # کاربر ریدایرکت میشه به همون آدرسی که بوده


def remove_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)
