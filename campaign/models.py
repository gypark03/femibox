from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.urls import reverse
from campaign.fields import ThumbnailImageField

# Create your models here.

class Cam (models.Model):
    category_label = (
        ('시위참여', '시위참여'),
        ('서명운동', '서명운동'),
        ('모금운동', '모금운동'),
    )
    category = models.CharField('CATEGORY', max_length=100, choices=category_label, blank=True)
    title = models.CharField('TITLE',max_length = 250)
    content = models.TextField(blank=True)
    image = ThumbnailImageField(null=True, blank=True, upload_to='with_us/photo/%Y/%m')
    create_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('campaign:campaign_detail', args=(self.id,))


