from django.db import models
from django.core.validators import MaxValueValidator


class Schedule(models.Model):
    title          = models.CharField('タイトル', max_length=255)
    duration_begin = models.DateField('期間開始日', null=True, blank=True)
    duration_end   = models.DateField('期間終了日', null=True, blank=True)
    total_budget   = models.PositiveIntegerField('予算合計', validators=[MaxValueValidator(1000000000)])
    place          = models.CharField('場所', max_length=255)
    datetime       = models.DateTimeField('日時', null=True, blank=True)
    memo           = models.TextField('メモ', null=True, blank=True)
    image          = models.ImageField('画像', null=True, blank=True, upload_to='schedule_images/')
    budget         = models.PositiveIntegerField('予算', validators=[MaxValueValidator(1000000000)])

    def __str__(self):
        return self.title
