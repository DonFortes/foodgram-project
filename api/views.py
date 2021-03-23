import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from dishes.models import Follow, User, Recipe
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods("POST")
def purchases(request):
    recipe_id = json.loads(request.body).get('id')
    if recipe_id is None:
        return JsonResponse({"success": False})
    recipe_id = int(recipe_id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.user not in recipe.basket.all():
        recipe.basket.add(request.user)
        recipe.save()
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
def subscriptions(request, id=None):
    if request.method == 'POST':
        user_id = json.loads(request.body).get("id")
        if user_id is None:
            return JsonResponse({"success": False})
        user_id = int(user_id)
        if User.objects.filter(pk=user_id).exists():
            following = User.objects.get(pk=user_id)
            if following not in request.user.following.all():
                request.user.following.add(following)
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


        # if user is None:
        #     Follow.objects.get_or_create(
        #         user=user,
        #         author=author,
        #     )
        #     return JsonResponse({"success": False})

    # elif request.method == 'DELETE':
    #     author = get_object_or_404(User, pk=id)
    #     user = request.user
    #     Follow.objects.filter(user=user, author=author).delete()

    # return JsonResponse({'success': 'true'})


@login_required
def favorites(request):

    return JsonResponse({'success': 'true'})


def single_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug)

    pass