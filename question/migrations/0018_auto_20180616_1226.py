# Generated by Django 2.0.4 on 2018-06-16 03:26

from django.db import migrations
import question.fields


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0017_auto_20180614_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qaa',
            name='image',
            field=question.fields.ThumbnailImageField(blank=True, null=True, upload_to='user_photo/%Y/%m'),
        ),
    ]
