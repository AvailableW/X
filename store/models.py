from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_media', blank=True)

    def get_absolute_url(self):
        return reverse('store:index')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True,
        blank=True, verbose_name='Категория',
        related_name='products'
    )
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    name = models.CharField(max_length=255, db_index=True)
    article = models.IntegerField(unique=True)
    date_add = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug, self.id])

    class Meta:
        ordering = ['-date_add']