# Generated by Django 4.2.2 on 2023-06-23 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_delete_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='場所')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='日時')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='plan_images/', verbose_name='画像')),
                ('budget', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='予算')),
            ],
        ),
    ]