from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # pass
    bio = models.ImageField('プロフィール画像', blank=True, null=True)
    birthday = models.DateField('誕生日', blank=True, null=True)
    login_id = models.CharField('ID', unique=True, max_length=20)