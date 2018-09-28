from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse
from product.fields import ThumbnailImageField

# Create your models here.

class box(models.Model):
    b_name = models.CharField(max_length = 100)
    price = models.IntegerField()
    image = ThumbnailImageField(upload_to='product/box/%Y/%m')
    content = models.TextField()

    def __str__(self):
        return self.b_name

    def get_absolute_url(self):
        return reverse('product:box_detail', args=(self, id,))

class goods(models.Model):
    category_label = (
        ('의류', '의류'),
        ('가방', '가방'),
        ('악세사리', '악세사리'),
        ('폰케이스', '폰케이스'),
        ('문구', '문구'),
        ('책', '책'),
    )
    category = models.CharField(max_length=100, choices=category_label)
    g_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = ThumbnailImageField(upload_to='product/goods/%Y/%m')
    content = models.TextField()

    def __str__(self):
        return self.g_name

    def get_absolute_url(self):
        return reverse('product:goods_detail', args=(self, id,))
