from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from .models import User, Recipe
from .forms import RecipeForm
from .service import get_tags, lets_paginate
from foodgram_project.settings import ITEMS_PER_PAGE


def index(request):
    tags = get_tags(request)
    recipe_list = Recipe.objects.filter(tags__name__in=tags).select_related(
        'author').prefetch_related('tags').distinct()

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            }
    )


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipe_list = author.recipe.all()

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'profile.html',
        {
            "page": page,
            "paginator": paginator,
            "author": author,
        }
    )


@login_required
def new_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(
            request.POST or None,
            files=request.FILES or None
            )
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            print(form)
            return redirect('index')
    print(request)
    return render(
        request,
        'new_recipe.html',
        {'form': form}
        )


def single_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "single_recipe.html", {'recipe': recipe})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    url = reverse('single_recipe', args={"slug": slug})

    if recipe.author != request.user:
        return redirect(url)

    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
        )

    if form.is_valid():
        form.save()
        return redirect(url)

    return redirect(url)


@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    url = reverse('single_recipe', args={"slug": slug})
    if recipe.author != request.user:
        return redirect(url)

    url = reverse('index')
    if recipe.author == request.user:
        recipe.delete()
    return redirect(url)


@login_required
def follows(request):
    authors = User.objects.filter(following__user=request.user)

    page, paginator = lets_paginate(request, authors)

    return render(
        request,
        'subscriptions.html',
        {
            'page': page, 'paginator': paginator
            }
    )


@login_required
def favorite(request):

    return render(
        request,
        'favorite.html',

    )
