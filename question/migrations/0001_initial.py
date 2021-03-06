# Generated by Django 2.0.4 on 2018-06-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='TITLE')),
                ('author', models.CharField(max_length=100, verbose_name='AUTHOR')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('view_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'faq',
                'verbose_name_plural': 'faqs',
                'ordering': ('-modify_date',),
            },
        ),
        migrations.CreateModel(
            name='QAA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='TITLE')),
                ('author', models.CharField(max_length=100, verbose_name='AUTHOR')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('view_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ('-modify_date',),
            },
        ),
    ]
