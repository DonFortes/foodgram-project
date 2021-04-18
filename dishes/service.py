from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from foodgram_project.settings import ITEMS_PER_PAGE
import csv
from .models import Ingredient, Tag, Volume
from django.db import transaction
from foodgram_project.services import log


def put_ingridients():
    with open('ingredients.csv', 'r', newline='', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            Ingredient.objects.get_or_create(
                name=row[0],
                measure=row[-1],
            )


def get_tags_from(request):
    return request.GET.getlist('tags')


def lets_paginate(request, list):
    paginator = Paginator(list, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator


@transaction.atomic
def save_recipe(request, form):

    recipe = form.save(commit=False)
    post = request.POST
    log.debug(post)

    recipe.author = request.user
    recipe.save()
    log.debug(dir(recipe))

    if post.get('breakfast') == 'on':
        recipe.tags.add(Tag.objects.get(name='breakfast'))
    if post.get('lunch') == 'on':
        recipe.tags.add(Tag.objects.get(name='lunch'))
    if post.get('dinner') == 'on':
        recipe.tags.add(Tag.objects.get(name='dinner'))

    ingredients = get_ingredients(request)
    ingredients_instances = []
    for ingredient_name, how_much in ingredients.items():
        ingredients_instances.append(Volume(
            recipe=recipe,
            ingredient=get_object_or_404(
                Ingredient, name__exact=ingredient_name),
            volume=int(how_much),
        ))
    Volume.objects.bulk_create(ingredients_instances)
    form.save_m2m()
    return recipe


def get_ingredients(request):
    post = request.POST
    ingredients = {}
    for key, name in post.items():
        if key.startswith("nameIngredient"):
            value = key.replace("name", "value")
            ingredients[name] = post[value]
    return ingredients
