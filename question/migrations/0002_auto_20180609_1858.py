# Generated by Django 2.0.4 on 2018-06-09 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ('-modify_date',), 'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQ'},
        ),
        migrations.AlterModelOptions(
            name='qaa',
            options={'ordering': ('-modify_date',), 'verbose_name': 'Q&A', 'verbose_name_plural': 'Q&A'},
        ),
    ]