# Generated by Django 2.0.4 on 2018-06-14 11:08

from django.db import migrations
import femiLetter.fields


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0014_auto_20180614_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qaa',
            name='image',
            field=femiLetter.fields.ThumbnailImageField(blank=True, null=True, upload_to='user_photo/%Y/%m'),
        ),
    ]