# Generated by Django 4.2.2 on 2023-06-23 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule'),
        ),
    ]
