from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Follow, User, Recipe
from .forms import RecipeForm


def index(request):
    recipe_list = Recipe.objects.all()

    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    # И еще теги как-то
    return render(
        request,
        'index.html',
        {
            'page': page, 'paginator': paginator
            }
    )


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipes = author.recipe.all()

    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if request.user.is_authenticated:
        user = request.user
        if Follow.objects.filter(user=user, author=author).exists():
            following = True
        else:
            following = False
        context = {
            'author': author,
            'page': page,
            'paginator': paginator,
            'following': following,
            'username': author,
        }
        return render(request, 'profile.html', context)
    return render(
        request,
        'profile.html',
        {'page': page, 'paginator': paginator, 'author': author}
    )


# @login_required
def new_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            print(form)
            return redirect('index')
    print(request)
    return render(request, 'new_recipe.html', {'form': form})


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

    pass


@login_required
def follows(request):
    recipe_list = Recipe.objects.filter(author__following__user=request.user)

    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        {
            'page': page, 'paginator': paginator
            }
    )
