from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=128,
        unique=True,
        verbose_name='Символьный ID'
    )

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category',
            args=[self.slug]
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=128,
        verbose_name='Символьный ID'
    )
    image = models.ImageField(
        upload_to='coffee/%Y/%m/%d',
        blank=True,
        verbose_name='Изображение'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    available = models.BooleanField(
        default=True,
        verbose_name='Наличие?'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлен'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменен'
    )

    category = models.ForeignKey(
        'Category',
        blank=True,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.id, self.slug]
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
