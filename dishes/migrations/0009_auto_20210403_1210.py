# Generated by Django 3.1.7 on 2021-04-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_auto_20210321_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, max_length=50, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='tag',
            name='visual_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отображаемое имя'),
        ),
    ]
