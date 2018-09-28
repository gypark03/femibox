# Generated by Django 2.0.4 on 2018-07-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0019_auto_20180702_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qaa',
            name='category',
            field=models.CharField(blank=True, choices=[('배송관련문의', '배송관련문의'), ('상품문의', '상품문의'), ('배송 후 교환반품', '배송 후 교환반품'), ('입금확인', '입금확인'), ('배송전 주문변경 및 취소', '배송전 주문변경 및 취소'), ('기타', '기타')], max_length=100, verbose_name='CATEGORY'),
        ),
    ]
