# Generated by Django 3.1.7 on 2021-04-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0009_auto_20210429_2223'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_follow'),
        ),
    ]
