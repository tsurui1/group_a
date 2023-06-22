<<<<<<< HEAD
# Generated by Django 4.2.2 on 2023-06-22 02:59
=======
# Generated by Django 4.2.2 on 2023-06-22 02:57
>>>>>>> 8a16ddc28f181579de255e0cb63630673a6f4fa1

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('duration', models.DateField(null=True, unique=True, verbose_name='期間')),
=======
                ('duration', models.DateField(blank=True, null=True, verbose_name='期間')),
>>>>>>> 8a16ddc28f181579de255e0cb63630673a6f4fa1
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('total_budget', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='予算合計')),
                ('place', models.CharField(max_length=255, verbose_name='場所')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='時間')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='schedule_images/', verbose_name='画像')),
                ('budget', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='予算')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.duration', verbose_name='期間')),
            ],
        ),
    ]
