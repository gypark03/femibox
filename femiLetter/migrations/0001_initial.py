# Generated by Django 2.0.4 on 2018-06-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('view_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('bad_count', models.IntegerField()),
            ],
        ),
    ]
