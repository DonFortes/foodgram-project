# Generated by Django 3.1.7 on 2021-04-18 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20210418_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volume',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volume', to='dishes.ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volume', to='dishes.recipe', verbose_name='Рецепт'),
        ),
    ]