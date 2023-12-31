from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='article_images/default_img.png', upload_to='article_images/', verbose_name='画像'),
        ),
    ]
