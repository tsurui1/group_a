from django.db import models
from schedule.models import Schedule
from accounts.models import CustomUser
from django.utils import timezone


class Chat(models.Model):
    groups     = models.ForeignKey(Schedule, related_name='chat_groups', on_delete=models.CASCADE)
    user       = models.ForeignKey(CustomUser, related_name='chat_users', on_delete=models.CASCADE, null=True, blank=True)
    comment    = models.TextField('コメント')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.comment
