# Generated by Django 5.0.4 on 2024-04-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='image.jpg', upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
