# Generated by Django 2.0.4 on 2018-06-13 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_qaa_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qaa',
            name='image',
        ),
    ]
