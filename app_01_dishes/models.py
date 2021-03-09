from django.contrib.auth import get_user_model
from django.db import models
# from . import choices


User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=50)
    measure = models.CharField(max_length=10)


class Tag(models.Model):
    title = models.CharField(max_length=50)


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="reciept",
        verbose_name='Автор'
        )
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(
        upload_to='app_01_dishes/',
        verbose_name='Картинка'
        )
    description = models.TextField(verbose_name='Текстовое описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингридиенты'
        )
    tag = models.ManyToManyField(Tag, verbose_name='Тэг')
    time = models.IntegerField()
    slug = models.SlugField(unique=True)
