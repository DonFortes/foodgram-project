from math import fabs

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404

from foodgram_project.settings import ITEMS_PER_PAGE

from .models import Ingredient, Tag, Volume


def get_and_filter_by_tags(request, list):
    tags = request.GET.getlist('tags')
    if tags:
        list = list.filter(tags__name__in=tags)
    return list, tags


def lets_paginate(request, list):
    paginator = Paginator(list, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator


@transaction.atomic
def save_recipe(request, form):

    recipe = form.save(commit=False)
    post = request.POST

    recipe.author = request.user
    recipe.save()

    if post.get('breakfast') == 'on':
        recipe.tags.add(get_object_or_404(Tag, name='breakfast'))
    if post.get('lunch') == 'on':
        recipe.tags.add(get_object_or_404(Tag, name='lunch'))
    if post.get('dinner') == 'on':
        recipe.tags.add(get_object_or_404(Tag, name='dinner'))

    ingredients = get_ingredients(request)
    ingredients_instances = []
    for ingredient_name, how_much in ingredients.items():
        ingredients_instances.append(Volume(
            recipe=recipe,
            ingredient=get_object_or_404(
                Ingredient, name__exact=ingredient_name),
            volume=fabs(int(how_much)),
        ))
    Volume.objects.bulk_create(ingredients_instances)
    form.save_m2m()
    return recipe


def get_ingredients(request):
    post = request.POST
    ingredients = {}
    for key, name in post.items():
        if key.startswith('nameIngredient'):
            value = key.replace('name', 'value')
            ingredients[name] = post[value]
    return ingredients
