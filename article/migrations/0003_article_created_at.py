# Generated by Django 4.2.2 on 2023-06-27 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]