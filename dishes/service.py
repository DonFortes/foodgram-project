from django.core.paginator import Paginator
from foodgram_project.settings import ITEMS_PER_PAGE
import csv
from .models import Ingredient


def put_ingridients():
    with open('ingredients.csv', 'r', newline='', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            Ingredient.objects.get_or_create(
                name=row[0],
                measure=row[-1],
            )


def get_tags_from(request):
    # TAGS = ['breakfast', 'lunch', 'dinner']
    return request.GET.getlist('tags')


def lets_paginate(request, list):
    paginator = Paginator(list, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator
