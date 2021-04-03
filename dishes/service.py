from django.core.paginator import Paginator
from foodgram_project.settings import ITEMS_PER_PAGE


def get_tags(request):
    return request.GET.getlist('tag', ('breakfast', 'lunch', 'dinner'))


def lets_paginate(request, list):
    paginator = Paginator(list, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator
