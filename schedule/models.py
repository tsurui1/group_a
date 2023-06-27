from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import CustomUser


class Schedule(models.Model):
    title          = models.CharField('タイトル', max_length=255)
    duration_begin = models.DateField('期間開始日', null=True, blank=True)
    duration_end   = models.DateField('期間終了日', null=True, blank=True)
    users          = models.ManyToManyField(CustomUser, blank=True)

    class Meta:
        ordering = ['duration_begin']

    def __str__(self):
        return self.title


class Plan(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True, blank=True)
    place    = models.CharField('場所', max_length=255)
    datetime = models.DateTimeField('日時', null=True, blank=True)
    memo     = models.TextField('メモ', null=True, blank=True)
    image    = models.ImageField('画像', null=True, blank=True, upload_to='plan_images/')
    budget   = models.PositiveIntegerField('予算', validators=[MaxValueValidator(1000000000)])

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.place
