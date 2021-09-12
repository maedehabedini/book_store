from django.urls import path
from .views import cart_detail, add_cart,remove_cart

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:id>/', add_cart, name='add_cart'),
    path('remove/<int:id>/', remove_cart, name='remove_cart'),

]
