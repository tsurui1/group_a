from django.db import models

class Article(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('画像')
    text = models.TextField('テキスト')
    date_begin = models.DateField('掲載日', blank=True, null=True)
    date_end = models.DateField('掲載日', blank=True, null=True)
    state_flag = models.BooleanField('表示', default=True)