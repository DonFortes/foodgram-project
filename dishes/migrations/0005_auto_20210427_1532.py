# Generated by Django 3.1.7 on 2021-04-27 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20210427_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volume',
            options={'verbose_name': 'Ингредиенты для рецептов', 'verbose_name_plural': 'Ингредиенты для рецептов'},
        ),
    ]
