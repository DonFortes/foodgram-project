# Generated by Django 3.1.7 on 2021-04-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20210430_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True, verbose_name='Ссылка'),
        ),
    ]
