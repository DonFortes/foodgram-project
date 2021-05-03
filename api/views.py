import json

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from dishes.models import Follow, Ingredient, Recipe, User


@login_required
@require_http_methods('POST')
def subscriptions(request):
    author_id = json.loads(request.body).get('id')
    if author_id is None:
        return JsonResponse({'success': False})
    author_id = int(author_id)
    author = get_object_or_404(User, pk=author_id)
    user = request.user
    if author != user:
        Follow.objects.get_or_create(
            user=user,
            author=author
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
@require_http_methods('DELETE')
def subscriptions_delete(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    user = request.user
    Follow.objects.filter(user=user, author=author).delete()
    return JsonResponse({'success': True})


@login_required
@require_http_methods('POST')
def favorites(request):
    recipe_id = json.loads(request.body).get('id')
    if recipe_id is None:
        return JsonResponse({'success': False})
    recipe_id = int(recipe_id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not request.user.favorites.filter(id=recipe_id).exists():
        recipe.is_favorite.add(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
@require_http_methods('DELETE')
def favorites_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.favorites.filter(id=recipe_id).exists():
        recipe.is_favorite.remove(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@require_http_methods('POST')
def purchases(request):
    recipe_id = json.loads(request.body).get('id')
    if recipe_id is None:
        return JsonResponse({'success': False})
    recipe_id = int(recipe_id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.is_authenticated:
        if not request.user.purchases.filter(id=recipe_id).exists():
            recipe.purchases.add(request.user)
            return JsonResponse({'success': True})
    else:
        basket = request.session.get('basket')
        if basket is None:
            basket = []
        basket.append(recipe_id)
        request.session['basket'] = basket
        return JsonResponse({'success': True})


@require_http_methods('DELETE')
def purchases_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.is_authenticated:
        if request.user.purchases.filter(id=recipe_id).exists():
            recipe.purchases.remove(request.user)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    else:
        basket = request.session.get('basket')
        if basket is None:
            basket = []
        basket.remove(recipe_id)
        request.session['basket'] = basket
        return JsonResponse({'success': True})


@login_required()
def ingredients(request):
    query = request.GET.get('query')
    if query:

        ingredients_from_db = list(Ingredient.objects.filter(
            name__startswith=query).values(
                title=F('name'), dimension=F('measure')))

    return JsonResponse(ingredients_from_db, safe=False)
