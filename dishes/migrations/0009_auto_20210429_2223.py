# Generated by Django 3.1.7 on 2021-04-29 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_auto_20210430_0114'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
