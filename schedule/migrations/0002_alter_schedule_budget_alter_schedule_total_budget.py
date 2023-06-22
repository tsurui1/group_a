# Generated by Django 4.2.2 on 2023-06-22 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='budget',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='予算'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='total_budget',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='予算合計'),
        ),
    ]
