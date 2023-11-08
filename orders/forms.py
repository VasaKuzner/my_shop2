from django import forms

from django.forms import ModelForm

from .get_nova import get_nova_poshta_data
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'adres_past', 'address', 'state']

        # #
        widgets = {
            'adres_past': forms.Select(attrs={
                "class": "adres-past-load",
            }),
            'address': forms.Select(attrs={
                "class": "address-load",
                "type": "search",
                'onchange': 'loadWarehouses()'
            }),
            'first_name': forms.TextInput(attrs={
                ' placeholder' : "Ведіть своє ім`я "
            }),
            'last_name': forms.TextInput(attrs={
                ' placeholder': "Ведіть своє прізвище "
            }),
            'surname': forms.TextInput(attrs={
                ' placeholder': "Ведіть своє побатькові  "
            }),
            'email': forms.EmailInput(attrs={
                ' placeholder': "Ведіть сій Email",
            }),
            'phonenumb': forms.TextInput(attrs={
                ' placeholder': "Ведіть свій номер телефону"
            }),

        }
        labels = {

            'first_name': "Ім'я",
             'last_name': 'Прізвище',
        }

        help_texts = {
            'address': 'Введіть вашу адресу доставки',
        }

        error_messages = {
            'email': {
            'required': 'Поле електронної пошти є обов"язковим.',
            'invalid': 'Будь ласка, введіть коректну адресу електронної пошти.',
        }}