from django.utils.http import urlencode
from django.urls import reverse
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


# @register.simple_tag
# def build_url(*args, **kwargs):
#     params = kwargs.pop('params', {})
#     url = reverse(*args, **kwargs)
#     if params:
#         url += '?' + urlencode(params)
#     return url


@register.simple_tag
def build_url(request, tags=None, name=None):
    tags = list(tags)

    if name in tags:
        tags.remove(name)
    else:
        tags.append(name)

    url = request.path_info
    url_params = '&'.join(f'tags={tag}' for tag in tags)
    return '?'.join((url, url_params))

    # url_params = []
    # for tag in tags:
    #     url_params.append('&'.join(f'tags={tag}'))

    # return str(*url_params)
