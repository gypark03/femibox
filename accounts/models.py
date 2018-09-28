from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=(('M', '남자'), ('W', '여자')), default='M', max_length=10, null=True)
    birth = models.CharField(max_length=6, null=True, help_text='주민등록번호 앞자리를 입력해주세요.')
    phone = models.CharField(max_length=11, null=True, unique=True, help_text='\'-\'를 제외한 휴대폰번호 11자리를 입력해 주세요.')