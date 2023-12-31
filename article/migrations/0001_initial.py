from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='', verbose_name='画像')),
                ('text', models.TextField(verbose_name='テキスト')),

                ('date_begin', models.DateField(blank=True, null=True, verbose_name='掲載開始日')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='掲載終了日')),
                ('state_flag', models.BooleanField(default=True, verbose_name='表示状況')),
                ('categories', models.ManyToManyField(blank=True, null=True, to='article.category')),

            ],
        ),
    ]
