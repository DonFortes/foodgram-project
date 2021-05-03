from django.contrib.auth import get_user_model
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

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Все ингредиенты'

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

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.visual_name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        db_index=True,
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
        related_name='recipes',
        through='Volume',
        verbose_name='Ингредиенты',
        db_index=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэги',
        db_index=True,
        blank=True,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True, db_index=True
    )
    cook_time = models.PositiveIntegerField(
        verbose_name='Время приготовления'
    )
    slug = models.SlugField(
        unique=True, verbose_name='Ссылка',
        blank=True, default='',
    )
    is_favorite = models.ManyToManyField(
        User, related_name='favorites',
        blank=True, verbose_name='Избранное',
    )
    purchases = models.ManyToManyField(
        User,
        related_name='purchases',
        blank=True,
        verbose_name='Корзина',
    )

    def save(self, *args, **kwargs):
        if self.slug == '':
            try:
                last_id = Recipe.objects.latest('pub_date').id
                num = last_id + 1
            except Recipe.DoesNotExist:
                num = 1

            self.slug = slugify(self.name) + f'_{str(num)}'

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return f'{self.name} от {self.author.username}'


class Volume(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='volumes',
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='volumes',
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    volume = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Ингредиент для рецептов'
        verbose_name_plural = 'Ингредиенты для рецептов'

    def __str__(self):
        return f'Ингредиент для рецепта: {self.recipe}'


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
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_follow')
        ]

    def __str__(self):
        return f'Подписка {self.user} на {self.author}'
