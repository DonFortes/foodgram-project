from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import RecipeForm
from .models import Recipe, Tag, User, Volume
from .service import get_and_filter_by_tags, lets_paginate, save_recipe


def index(request):
    all_tags = Tag.objects.all()
    recipe_list = Recipe.objects.select_related(
        'author').prefetch_related('tags').distinct()
    list, tags = get_and_filter_by_tags(request, recipe_list)
    page, paginator = lets_paginate(request, list)
    return render(request, 'dishes/index.html', {'page': page,
                                                 'paginator': paginator,
                                                 'tags': tags,
                                                 'all_tags': all_tags,
                                                 })


def profile(request, username):
    all_tags = Tag.objects.all()
    author = get_object_or_404(User, username=username)
    recipe_list = author.recipes.all()
    list, tags = get_and_filter_by_tags(request, recipe_list)
    page, paginator = lets_paginate(request, list)
    return render(request, 'dishes/profile.html', {'page': page,
                                                   'paginator': paginator,
                                                   'tags': tags,
                                                   'all_tags': all_tags,
                                                   'author': author,
                                                   })


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        recipe = save_recipe(request, form)
        return redirect('single_recipe', slug=recipe.slug)
    return render(request, 'dishes/new_recipe.html', {'form': form})


def single_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'dishes/single_recipe.html', {'recipe': recipe})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    url = redirect('single_recipe', slug=slug)
    if recipe.author != request.user:
        if not request.user.is_superuser:
            return url
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)
    if form.is_valid():
        Volume.objects.filter(recipe=recipe).delete()
        save_recipe(request, form)
        return url
    used_tags_queryset = recipe.tags.values_list()
    used_tags = []
    for tag in used_tags_queryset:
        used_tags.append(tag[1])
    used_ingredients = recipe.volumes.all
    edit = True
    return render(request,
                  'dishes/new_recipe.html',
                  {'form': form, 'edit': edit,
                   'recipe': recipe,
                   'used_ingredients': used_ingredients,
                   'used_tags': used_tags})


@ login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    url = reverse('index')
    if recipe.author == request.user or request.user.is_superuser:
        recipe.delete()
        return redirect(url)
    url = reverse('single_recipe', kwargs={'slug': slug})
    if recipe.author != request.user:
        return redirect(url)


@ login_required
def follows(request):
    authors = User.objects.filter(following__user=request.user)
    page, paginator = lets_paginate(request, authors)
    return render(request, 'dishes/subscriptions.html',
                  {'page': page,
                   'paginator': paginator})


@ login_required
def favorite(request):
    all_tags = Tag.objects.all()
    recipe_list = request.user.favorites.select_related(
        'author').prefetch_related('tags').distinct()
    list, tags = get_and_filter_by_tags(request, recipe_list)
    page, paginator = lets_paginate(request, list)
    return render(request, 'dishes/favorite.html', {'page': page,
                                                    'paginator': paginator,
                                                    'tags': tags,
                                                    'all_tags': all_tags,
                                                    })


def shoplist(request):
    if request.user.is_authenticated:
        recipe_list = request.user.purchases.all()
    else:
        basket = request.session.get('basket')
        if basket is not None:
            recipe_list = Recipe.objects.filter(id__in=basket)
        else:
            recipe_list = []
    return render(request, 'dishes/shoplist.html',
                  {'recipe_list': recipe_list})


def download_file(request):
    if request.user.is_authenticated:
        recipes = request.user.purchases.all()
    else:
        recipes = Recipe.objects.filter(id__in=request.session.get('basket'))
    if not recipes:
        return render(request, 'misc/404.html', status=404)
    volumes = Volume.objects.filter(recipe__in=recipes)
    text = 'Список покупок:\n\n'

    ingredients_dict = defaultdict(int)
    for ing in sorted(volumes, key=lambda volume: volume.ingredient.name):
        key = f'{ing.ingredient.name}, {ing.ingredient.measure}'
        ingredients_dict[key] += ing.volume
    ingredients_dict = ingredients_dict
    for key, value in ingredients_dict.items():
        text += (f'{key}: {value}\n')

    response = HttpResponse(text, content_type='text/plain')
    filename = 'shop_list.txt'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
