# Generated by Django 3.1.7 on 2021-03-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Ссылка'),
        ),
    ]
