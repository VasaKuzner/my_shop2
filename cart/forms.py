

from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кількість',
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

    size = forms.CharField(max_length=100, required=False, label='Розмір')  # Додайте поле для розміру
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int , label='Кількість ') # для перетворення введення в ціле чтсло
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)