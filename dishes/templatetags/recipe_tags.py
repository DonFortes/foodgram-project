from django import template
from dishes.models import Recipe
from foodgram_project.settings import AUTHOR_RECIPE

register = template.Library()

# Не забывать добавлять {% load recipe_tags %} в шаблон


@register.simple_tag
def total_recipes(author):
    return Recipe.objects.filter(author=author).count()


@register.simple_tag
def recipes_for_subscriptions(author, count=AUTHOR_RECIPE):
    latest_recipes = Recipe.objects.filter(author=author)[:count]
    return latest_recipes


@register.simple_tag
def get_recipes_of(author):
    return Recipe.objects.filter(author=author)
