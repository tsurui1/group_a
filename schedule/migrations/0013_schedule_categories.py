# Generated by Django 4.2.2 on 2023-06-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_user'),
        ('schedule', '0012_remove_schedule_total_budget_schedule_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='article.category'),
        ),
    ]
