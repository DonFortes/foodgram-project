import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from dishes.models import Follow, User, Recipe
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods("POST")
def purchases(request):
    recipe_id = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user not in recipe.basket.all():
        recipe.basket.add(request.user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


@login_required
@require_http_methods("DELETE")
def purchases_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user in recipe.basket.all():
        recipe.basket.remove(request.user)
        return JsonResponse({'success': True})


@login_required
@require_http_methods("POST")
def subscriptions(request, id=None):
    author_id = int(json.loads(request.body).get("id"))
    author = get_object_or_404(pk=author_id)
    user = request.user
    if author != user:
        Follow.objects.get_or_create(
            user=user,
            author=author
        )
        return JsonResponse({'success': True})
    return JsonResponse({"success": False})



@login_required
def subscriptions_delete(request, id=None):
    
    return JsonResponse({'success': 'true'})

@login_required
def favorites(request):

    return JsonResponse({'success': 'true'})


def single_recipe(request, slug):

    return JsonResponse({'success': 'true'})