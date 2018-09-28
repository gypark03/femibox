from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from question.fields import ThumbnailImageField

# Create your models here.

class QAA(models.Model):
    category_label = (
        ('배송관련문의', '배송관련문의'),
        ('상품문의', '상품문의'),
        ('배송 후 교환반품', '배송 후 교환반품'),
        ('입금확인', '입금확인'),
        ('배송전 주문변경 및 취소', '배송전 주문변경 및 취소'),
        ('기타', '기타'),
    )
    category = models.CharField('CATEGORY', max_length=100, choices=category_label, blank=True)
    title = models.CharField('TITLE', max_length=100)
    author = models.CharField('NAME', max_length=100)
    password = models.CharField('PASSWORD', max_length=50, null=True)
    content = models.TextField('CONTENT')
    image = ThumbnailImageField('FILE', null=True, blank=True, upload_to='user_photo/%Y/%m')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'Q&A'
        verbose_name_plural = 'Q&A'
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:QAA_detail', args=(self.id,))



class FAQ(models.Model):
    category_label = (
            ('배송관련문의', '배송관련문의'),
            ('상품문의', '상품문의'),
            ('배송 후 교환반품', '배송 후 교환반품'),
            ('입금확인', '입금확인'),
            ('배송전 주문변경 및 취소', '배송전 주문변경 및 취소'),
            ('기타', '기타'),
        )
    category = models.CharField('CATEGORY',  choices=category_label,max_length=100, blank=True)
    title = models.CharField('TITLE', max_length=100)
    content = models.TextField('CONTENT')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:FAQ_detail', args=(self.id,))

