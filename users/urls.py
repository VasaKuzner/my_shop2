
from django.urls import path , include

from .views import *

app_name = 'users'

urlpatterns = [
    # path('', include("django.contrib.auth.urls")),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('', order_create, name='order_create' ),
    path('logout_user/', logout_user, name='logout_user'),

]


