# Generated by Django 2.0.4 on 2018-06-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0015_auto_20180614_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qaa',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='NAME'),
        ),
        migrations.AlterField(
            model_name='qaa',
            name='content',
            field=models.TextField(blank=True, verbose_name='CONTENT'),
        ),
        migrations.AlterField(
            model_name='qaa',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PASSWORD'),
        ),
    ]