# Generated by Django 2.0.4 on 2018-06-12 07:48

from django.db import migrations
import femiLetter.fields


class Migration(migrations.Migration):

    dependencies = [
        ('femiLetter', '0002_auto_20180612_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='memos',
            name='image',
            field=femiLetter.fields.ThumbnailImageField(null=True, upload_to='photo/%Y/%m'),
        ),
    ]
