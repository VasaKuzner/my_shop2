from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, ProducPhoto
from .cart import Cart
from .forms import CartAddProductForm


@require_POST # декоратор що дозволити лише запит POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)# Отримуємл екземпляр продукту із заданим ID

    form = CartAddProductForm(request.POST,)

    if form.is_valid():
        cd = form.cleaned_data
        size = cd['size']  # Отримайте розмір із форми
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 size=size)

    return redirect('cart:cart_detail')

# Видалення товарів з кошика
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# відображення кошика та його товарівa
def cart_detail(request):
    cart = Cart(request)
    #
    # for cr in cart:
    #
    #     print(cr)
    return render(request, 'cart/detail.html', {'cart': cart,})