# Generated by Django 3.1.7 on 2021-04-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='recipe', to='dishes.Tag', verbose_name='Тэги'),
        ),
    ]