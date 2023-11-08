# from django.template.defaulttags import url
from django.urls import path , include


from . import views
from .views import *

app_name = 'orders'

urlpatterns = [
    path('', order_create, name='order_create' ),
    path('admin/order/orders/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),


]


