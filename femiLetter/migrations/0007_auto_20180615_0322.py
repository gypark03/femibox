# Generated by Django 2.0.4 on 2018-06-14 18:22

from django.db import migrations
import femiLetter.fields


class Migration(migrations.Migration):

    dependencies = [
        ('femiLetter', '0006_auto_20180614_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memos',
            name='image',
            field=femiLetter.fields.ThumbnailImageField(blank=True, null=True, upload_to='photo/%Y/%m'),
        ),
    ]
