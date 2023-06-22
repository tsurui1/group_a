from django.db import models
from django.core.validators import MaxValueValidator


class Duration(models.Model):
    duration     = models.DateField('期間', null=True, blank=True)

    def __str__(self):
        return self.duration


class Schedule(models.Model):
    title        = models.CharField('タイトル', max_length=255)
    total_budget = models.IntegerField('予算合計', validators=[MaxValueValidator(1000000000)])
    place        = models.CharField('場所', max_length=255)
    date         = models.ForeignKey(Duration, on_delete=models.CASCADE, verbose_name='期間')
    time         = models.TimeField('時間', null=True, blank=True)
    memo         = models.TextField('メモ', null=True, blank=True)
    image        = models.ImageField('画像', null=True, blank=True, upload_to='schedule_images/')
    budget       = models.IntegerField('予算', validators=[MaxValueValidator(1000000000)])

    def __str__(self):
        return self.title
