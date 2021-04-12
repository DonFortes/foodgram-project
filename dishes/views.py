from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from .models import User, Recipe, Tag
from .forms import RecipeForm
from .service import lets_paginate, get_tags_from


def index(request):

    tags = get_tags_from(request)
    all_tags = Tag.objects.all()

    recipe_list = Recipe.objects.select_related(
        'author').prefetch_related('tags').distinct()

    if tags:
        recipe_list = recipe_list.filter(tags__name__in=tags)

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
        }
    )


def profile(request, username):
    tags = get_tags_from(request)
    all_tags = Tag.objects.all()

    author = get_object_or_404(User, username=username)
    recipe_list = author.recipe.all()

    if tags:
        recipe_list = recipe_list.filter(tags__name__in=tags)

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'profile.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
            'author': author,
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
    return render(request, 'single_recipe.html', {'recipe': recipe})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    url = reverse('single_recipe', args={'slug': slug})

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
    url = reverse('single_recipe', args={'slug': slug})
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
    tags = get_tags_from(request)
    all_tags = Tag.objects.all()

    recipe_list = request.user.favorite.select_related(
        'author').prefetch_related('tags').distinct()

    if tags:
        recipe_list = recipe_list.filter(tags__name__in=tags)

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'favorite.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
        }
    )


@login_required
def shoplist(request):
    recipe_list = request.user.basket.all()

    page, paginator = lets_paginate(request, recipe_list)

    return render(
        request,
        'shoplist.html',
        {
            'page': page,
            'paginator': paginator,
        }
    )
