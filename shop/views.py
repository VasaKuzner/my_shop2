import requests
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.db.models import Count
from django.db.models.functions import Substr

from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
from .models import Category, Product, ProducPhoto

from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()


    products = Product.objects.all()



    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    unique_vendor_codes = products.values('vendor_code').distinct()
    # print(unique_vendor_codes)
    # Фільтруємо продукти, вибираючи тільки перший продукт для кожного vendor_code
    # unique_products = []
    # seen_vendor_codes = set()
    #
    # for product in products:
    #     if product.vendor_code not in seen_vendor_codes:
    #
    #         unique_products.append(product)
    #         seen_vendor_codes.add(product.vendor_code)
    #
    # products = unique_products

    products_per_page = 20

    paginator = Paginator(products, products_per_page)

    page = request.GET.get('page')



    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        # If 'page' is not an integer, show the first page.
        products = paginator.page(1)

    except EmptyPage:
        # If 'page' is out of range (e.g., 9999), show the last page.

        products = paginator.page(paginator.num_pages)


    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                )
    products = Product.objects.all()

    # products = products.annotate(art_prefix=vendor_code))
    # related_products = products.filter(art_prefix=vendor_code)
    # # Отримайте art_prefix продукта product
    # product_art_prefix = product.art[:4]


    # Знайдіть всі продукти зі співпадаючим art_prefix
    # related_products = products.filter(art_prefix=product_art_prefix).exclude(id=product.id)

    # related_products = products.filter(art_prefix=product_art_prefix).exclude(id=product.id)
    # for rt in related_products:
    #     if rt.param1 == rt.param1:
    #         print()
    #     print(rt.param1)

    # all_products = [product] + list(related_products)

    # print(product.photo)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   # 'all_products': all_products,
                   'cart_product_form': cart_product_form,
                   })





def about(request, ):
    return render(request, 'shop/about.html')

def policy(request):
    return render(request, 'shop/policy.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отримуємо дані з форми
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            # Складаємо повідомлення для відправки на email адміністратору
            subject = f'Новий контакт від {name}'
            message = f'Ім\'я: {name}\nEmail: {email}\nНомер телефону: {phone_number}\nПовідомлення:\n{message}'
            from_email = 'your_email@gmail.com'  # Адреса електронної пошти, з якої відправляється повідомлення

            # Адреса електронної пошти адміністратора
            admin_email = 'vasakuzner@gmail.com' # vasakuzner@gmail.com

            # Відправляємо email
            send_mail(subject, message, from_email, [admin_email])

            # Після відправки, перенаправляємо користувача на іншу сторінку

            return HttpResponseRedirect(reverse('shop:product_list',))  # Замініть 'success_page' на URL вашої сторінки успіху

    else:
        form = ContactForm()

    return render(request, 'shop/contacts.html', {'form': form})

def term_of_use(request):
    return render(request, 'shop/term_of_use.html')


def exchange(request, ):
    return render(request, 'shop/exchange.html')

def delivery_payment(request, ):
    return render(request, 'shop/delivery_payment.html')



# from django.shortcuts import render
# import xml.etree.ElementTree as ET
#
#
# def parse_and_display(request):
#     xml_url = "https://nosisvoe.com.ua/fua.xml"
#     response = requests.get(xml_url)
#
#     if response.status_code == 200:
#         root = ET.fromstring(response.content)
#
#         if root:
#             products_by_category = {}  # Словник для збереження товарів по категоріях
#
#             for item in root.findall(".//item"):
#                 category = item.find("category").text
#                 product = {
#                     "name": item.find("name").text,
#                     "description": item.find("description").text if item.find("description") is not None else "",
#                     "price": item.find("price").text,
#                     "param": item.find("param").text,
#                     "category": item.find("category").text,
#                     "param1": item.find("param").text,
#                     "old_price": item.find("old").text,
#
#                     "vendor": item.find("vendor").text,
#                     "image": item.find("image").text if item.find("image") is not None else "",
#                     "params": [param.text for param in item.findall("param")],
#                     # ... other fields you want to extract
#                 }
#
#                 if category in products_by_category:
#                     if len(products_by_category[category]) < 20:  # Limit to 20 products per category
#                         products_by_category[category].append(product)
#                     # products_by_category[category].append(product)
#                 else:
#                     products_by_category[category] = [product]
#
#             return render(request, "shop/product/new_lists.html", {"products_by_category": products_by_category})
#     else:

#         print("Failed to retrieve XML")