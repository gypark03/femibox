# Generated by Django 2.0.4 on 2018-07-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('femiLetter', '0007_auto_20180615_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memos',
            name='bad_count',
        ),
    ]
