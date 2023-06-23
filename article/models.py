from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリ', max_length=255, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('画像', upload_to='article_images/')
    text = models.TextField('テキスト')
    date_begin = models.DateField('掲載開始日', blank=True, null=True)
    date_end = models.DateField('掲載終了日', blank=True, null=True)
    state_flag = models.BooleanField('表示状況', default=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.title[:10]