# Generated by Django 3.1.7 on 2021-03-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20210318_0919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-pub_date'], 'verbose_name': 'рецепт', 'verbose_name_plural': 'рецепты'},
        ),
    ]
