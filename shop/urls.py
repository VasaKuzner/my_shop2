
from django.urls import path , include

from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('exchange/', exchange, name='exchange'),
    path('policy/', policy, name='policy'),
    path('contacts/', contacts, name='contacts'),
    path('term_of_use/', term_of_use, name='term_of_use'),
    path('delivery_payment/', delivery_payment, name='delivery_payment'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),


]


# path('', parse_and_display, name='new_lists'),