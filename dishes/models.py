from logging import exception

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.text import slugify as django_slugify

User = get_user_model()


alphabet = {'а': 'a', 'б': 'b', 'в': 'v',
            'г': 'g', 'д': 'd', 'е': 'e',
            'ё': 'yo', 'ж': 'zh', 'з': 'z',
            'и': 'i', 'й': 'j', 'к': 'k',
            'л': 'l', 'м': 'm', 'н': 'n',
            'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts',
            'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ы': 'i', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',)
    measure = models.CharField(
        max_length=255,
        verbose_name='Единица измерения',
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
    )
    visual_name = models.CharField(
        max_length=50,
        verbose_name='Отображаемое имя',
        blank=True,
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет',
        blank=True,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="recipe",
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        db_index=True
    )
    image = models.ImageField(
        upload_to='app_01_dishes/',
        verbose_name='Картинка',
    )
    description = models.TextField(
        verbose_name='Текстовое описание'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe',
        through='Volume',
        verbose_name='Ингредиенты',
        db_index=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipe',
        verbose_name='Тэги',
        db_index=True,
        blank=True,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True, db_index=True
    )
    cook_time = models.IntegerField(
        verbose_name='Время приготовления'
    )
    slug = models.SlugField(
        unique=True, verbose_name='Ссылка',
        blank=True, default='',
    )
    is_favorite = models.ManyToManyField(
        User, related_name='favorite',
        blank=True, verbose_name='Избранное',
    )
    basket = models.ManyToManyField(
        User,
        related_name='basket',
        blank=True,
        verbose_name='Корзина',
    )

    def save(self, *args, **kwargs):

        try:
            last_id = Recipe.objects.latest('pub_date').id
            num = last_id + 1
        except ObjectDoesNotExist:
            num = 1
            pass

        self.slug = slugify(self.name) + f'_{str(num)}'

        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return f'Рецепт {self.name} от {self.author.username}'


class Volume(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='volume',
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='volume',
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    volume = models.IntegerField()


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        null=True
    )

    class Meta:
        unique_together = ["user", "author"]
