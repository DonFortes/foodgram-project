# Generated by Django 3.1.7 on 2021-04-27 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_auto_20210427_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volume',
            options={'verbose_name': 'Ингредиент для рецептов', 'verbose_name_plural': 'Ингредиенты для рецептов'},
        ),
    ]