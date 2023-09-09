from django import forms
from shop.models import *

#   Исправить существующий цикл: покупка максимального доступного кол-во
PRODUCT_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(len(Product.objects.all()))
] # Тут надо проверки по наличию и конкретным товарам!


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
