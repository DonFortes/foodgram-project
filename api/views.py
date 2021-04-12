import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from dishes.models import Follow, User, Recipe
from django.views.decorators.http import require_http_methods


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


@login_required
@require_http_methods("POST")
def purchases(request):
    recipe_id = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.is_authenticated:
        if request.user not in recipe.shoplist.all():
            recipe.shoplist.add(request.user)
            return JsonResponse({'success': True})
    else:
        shoplist = request.session.get('shoplist')
        if shoplist is None:
            shoplist = []
        shoplist.append(recipe_id)
        request.session['shoplist'] = shoplist
        return JsonResponse({'success': True})


@login_required
@require_http_methods("DELETE")
def purchases_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user in recipe.shoplist.all():
        recipe.shoplist.remove(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
