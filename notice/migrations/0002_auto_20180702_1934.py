# Generated by Django 2.0.4 on 2018-07-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='category',
            field=models.CharField(blank=True, choices=[('기사', '기사'), ('칼럼', '칼럼'), ('안내', '안내')], default='1', max_length=100, verbose_name='CATEGORY'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100, verbose_name='TITLE'),
        ),
    ]
