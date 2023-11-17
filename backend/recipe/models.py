from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    """Модель тегов. """

    name = models.CharField(
        'Название тега', max_length=150, unique=True)
    color = models.CharField('Цвет',
                             help_text='Цвет тега в шестнадцетиричном виде',
                             max_length=7)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиентов. """

    name = models.CharField(
        'Название ингридиента', max_length=50)
    unit = models.CharField(
        'Единица измерения', max_length=20)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.unit}'


class Recipe(models.Model):
    """Модель рецептов. """

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes')
    name = models.CharField('Название рецепта',
                            max_length=50)
    description = models.TextField('Описание',
                                   max_length=1000)
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления блюда')
    tags = models.ManyToManyField(Tag, verbose_name='Теги',
                                  validators=(MinValueValidator(1)))
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингридиенты',
        related_name='recipes')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Модель избранное."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites',
        verbose_name='Пользователь')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт',
        related_name='favorites')

    class Meta:
        verbose_name = 'избранное'
        verbose_name_plural = 'избранное'
        constraints = [
            models.UniqueConstraint(
                fields=('recipe', 'user'), name='unique_favorite')
        ]

    def __str__(self):
        return f'{self.recipe.name}, {self.user.username},'

# class IngredientRecipeModel(models.Model):
#     recipe = models.ForeignKey(Recipe,
#                                verbose_name='Рецепт',
#                                on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient,
#                                    verbose_name='Ингредиент',
#                                    on_delete=models.PROTECT)
#
#     class Meta:
#         verbose_name = ("Ингредиенты")
#         verbose_name_plural = ("Ингредиенты")
#
#     def __str__(self):
#         return self.name
