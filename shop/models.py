from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category_id = models.CharField(max_length=200, db_index=True)



    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    offer_id = models.CharField(max_length=50, unique=True)  # Додав поле offer_id
    group = models.CharField(max_length=50, blank=True, null=True)
    available = models.BooleanField(default=True , null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=800, blank=True, null=True)
    vendor_code = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    country_of_manufacture = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    decoration = models.CharField(max_length=50, blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)
    fastener = models.CharField(max_length=50, blank=True, null=True)
    fabric_type = models.CharField(max_length=50, blank=True, null=True)
    upper_material = models.CharField(max_length=50, blank=True, null=True)
    filler_material = models.CharField(max_length=50, blank=True, null=True)
    lining_material = models.CharField(max_length=50, blank=True, null=True)
    model_features = models.CharField(max_length=50, blank=True, null=True)
    fabric_features = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=50, blank=True, null=True)
    composition = models.CharField(max_length=50, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    cut_features = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    # color_group = models.CharField(max_length=50, blank=True, null=True)
    price_segment = models.CharField(max_length=50, blank=True, null=True)
    # size = models.CharField(max_length=50, blank=True, null=True)
    size = models.JSONField(blank=True, null=True, )
    quantity_in_stock = models.PositiveIntegerField(blank=True, null=True)
    picture1 = models.CharField(max_length=200, blank=True, null=True)
    picture2 = models.CharField(max_length=200, blank=True, null=True)
    picture3 = models.CharField(max_length=200, blank=True, null=True)
    picture4 = models.CharField(max_length=200, blank=True, null=True)
    picture5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class ProducPhoto(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/$d/", verbose_name="Фото")
    is_main = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.product.id,])
