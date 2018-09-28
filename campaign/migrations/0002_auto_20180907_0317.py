# Generated by Django 2.0.4 on 2018-09-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cam',
            name='category',
            field=models.CharField(blank=True, choices=[('서명운동', '서명운동'), ('모금운동', '모금운동')], max_length=100, verbose_name='CATEGORY'),
        ),
        migrations.AlterField(
            model_name='cam',
            name='title',
            field=models.CharField(max_length=250, verbose_name='TITLE'),
        ),
    ]