from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order






def order_create(request):
    cart = Cart(request) # тут  ми отримуємо поточний кошик із сесії
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            # очистка корзины
            cart.clear()

            # запуск асинхронной задачи
            order_created.delay(order.id)
            # Отримати дані про адреси і номери відділень "Нової Пошти"

            return render(request, 'orders/order/created.html',
                          {'order': order, })
    else:
        form = OrderCreateForm # тут відображається шаблон orders/order/create.html

        print(f"my form is {form}")


    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/detail.html',
                  {'order': order} )



