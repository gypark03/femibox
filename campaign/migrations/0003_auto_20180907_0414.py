# Generated by Django 2.0.4 on 2018-09-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20180907_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cam',
            name='category',
            field=models.CharField(blank=True, choices=[('시위참여', '시위참여'), ('서명운동', '서명운동'), ('모금운동', '모금운동')], max_length=100, verbose_name='CATEGORY'),
        ),
    ]
