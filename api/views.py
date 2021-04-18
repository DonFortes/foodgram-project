import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from loguru import logger
from dishes.models import Follow, Ingredient, User, Recipe
from django.views.decorators.http import require_http_methods
from foodgram_project.services import log


@login_required
@require_http_methods("POST")
def subscriptions(request):
    author_id = int(json.loads(request.body).get("id"))
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
@require_http_methods("DELETE")
def subscriptions_delete(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    user = request.user
    if Follow.objects.filter(user=user, author=author).exists():
        Follow.objects.filter(user=user, author=author).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
@require_http_methods("POST")
def favorites(request):
    recipe_id = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user not in recipe.is_favorite.all():
        recipe.is_favorite.add(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
@require_http_methods("DELETE")
def favorites_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user in recipe.is_favorite.all():
        recipe.is_favorite.remove(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@require_http_methods("POST")
def purchases(request):
    recipe_id = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.is_authenticated:
        if request.user not in recipe.basket.all():
            recipe.basket.add(request.user)
            return JsonResponse({'success': True})
    else:
        basket = request.session.get('basket')
        if basket is None:
            basket = []
        basket.append(recipe_id)
        request.session['basket'] = basket
        return JsonResponse({'success': True})


@require_http_methods("DELETE")
def purchases_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.is_authenticated:
        if request.user in recipe.basket.all():
            recipe.basket.remove(request.user)
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
    ingredients = []
    query = request.GET.get('query')
    log.debug(query)
    if query:
        ingredients_from_db = Ingredient.objects.filter(name__startswith=query)
        for db_ingredient in ingredients_from_db:
            log.debug(db_ingredient.name)
            log.debug(db_ingredient.measure)
            js_response = {
                "title": db_ingredient.name,
                "dimension": db_ingredient.measure,
            }
            log.debug(js_response)
            ingredients.append(js_response)

    return JsonResponse(ingredients, safe=False)
