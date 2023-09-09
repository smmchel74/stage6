from django.db import models
from shop.models import Product


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес'
    )
    postal_code = models.CharField(
        max_length=32,
        verbose_name='Почтовый индекс'
    )
    city = models.CharField(
        max_length=128,
        verbose_name='Город'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )
    paid = models.BooleanField(
        default=False,
        verbose_name='Статус оплаты'
    )

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return f'Заказ: {self.id}'

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(
        'Order',
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Цена'
    )

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
