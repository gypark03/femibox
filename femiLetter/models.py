from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.urls import reverse
from femiLetter.fields import ThumbnailImageField

# Create your models here.

class Memos (models.Model):
    title_label = (
        ('사람', '사람'),
        ('#Me Too', '#Me Too'),
        ('토닥토닥', '토닥토닥'),
    )

    title = models.CharField(max_length = 250)
    author = models.CharField(max_length = 30)
    content = models.TextField(blank=True)
    image = ThumbnailImageField(null=True, blank=True, upload_to='photo/%Y/%m')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(null=True, blank=True)
    good_count = models.IntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('femiLetter:letter_detail', args=(self.id,))
