from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measure = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="reciept",
        verbose_name='Автор'
        )
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        db_index=True
        )
    image = models.ImageField(
        upload_to='app_01_dishes/',
        verbose_name='Картинка'
        )
    description = models.TextField(
        verbose_name='Текстовое описание'
        )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Volume',
        verbose_name='Ингридиенты',
        db_index=True
        )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Тэг',
        db_index=True
        )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True, db_index=True
        )
    cook_time = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Volume(models.Model):
    id_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        )
    id_ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
        )
    volume = models.IntegerField()
