from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

# Create your models here.

class notice(models.Model):
    category_label = (
        ('기사','기사' ),
        ('칼럼', '칼럼'),
        ('안내', '안내'),
    )
    category = models.CharField('CATEGORY', max_length=100, choices=category_label, default='1', blank=True)
    title = models.CharField('TITLE', max_length=100)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)

    class Meta:
        verbose_name = 'notice'
        verbose_name_plural = 'notice'
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice:notice_detail', args=(self.id,))
