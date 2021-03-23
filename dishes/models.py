from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
# from autoslug import AutoSlugField
# from uuslug import slugify


User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',)
    measure = models.CharField(
        max_length=10,
        verbose_name='Единица измерения',
        )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
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
        verbose_name='Ингридиенты',
        db_index=True
        )
    tag = models.ManyToManyField(
        Tag,
        related_name='recipe',
        verbose_name='Тэг',
        db_index=True,
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
    # slug = AutoSlugField(
    #     populate_from="name", allow_unicode=True, unique=True,
    #     editable=True, verbose_name="ссылка", blank=True,
    #     )
    is_favorite = models.ManyToManyField(
        User, related_name='favorite',
        blank=True, verbose_name='Избранное',
        )
    basket = models.ManyToManyField(
        User,
        related_name='basket',
        # through='Basket',
        blank=True,
        verbose_name='Корзина',
        )

    # def save(self, *args, **kwargs):
    #     self.slug = uuslug(self.name, instance=self)
    #     super(Recipe, self).save(*args, **kwargs)


    # my_string = str(slug).translate(
    #     str.maketrans(
    #         "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    #         "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
    #     ))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.my_string)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return f'Рецепт {self.name} от {self.author.username}'


class Volume(models.Model):
    id_recipe = models.ForeignKey(
        Recipe,
        related_name='volume',
        on_delete=models.CASCADE,
        verbose_name='id рецепта',
        )
    id_ingredient = models.ForeignKey(
        Ingredient,
        related_name='volume',
        on_delete=models.CASCADE,
        verbose_name='id ингридиента',
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
