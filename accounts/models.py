from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # pass
    bio = models.ImageField('プロフィール画像', blank=True, null=True, upload_to='accounts_images/')
    birthday = models.DateField('誕生日', blank=True, null=True)