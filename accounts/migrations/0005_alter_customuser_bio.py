# Generated by Django 4.2.2 on 2023-06-23 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_customuser_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.ImageField(blank=True, null=True, upload_to='accounts_images/', verbose_name='プロフィール画像'),
        ),
    ]
