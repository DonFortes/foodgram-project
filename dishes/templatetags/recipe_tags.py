from django import template

from dishes.models import Recipe
from foodgram_project.settings import AUTHOR_RECIPE

register = template.Library()


@register.simple_tag
def total_recipes(author):
    return Recipe.objects.filter(author=author).count()


@register.simple_tag
def recipes_for_subscriptions(author, count=AUTHOR_RECIPE):
    latest_recipes = Recipe.objects.filter(author=author)[:count]
    return latest_recipes


@register.simple_tag
def get_recipes_of(author):
    return Recipe.objects.filter(author=author)


@register.simple_tag
def build_url(request, tags=None, name=None, page=None):
    tags = list(tags)
    url = request.path_info

    if page is not None:
        page_params = f'page={page}'
        url_params = '&'.join(f'tags={tag}' for tag in tags)
        all_params = f'{page_params}&{url_params}'
        return '?'.join((url, all_params))

    if name in tags:
        tags.remove(name)
    else:
        tags.append(name)

    url_params = '&'.join(f'tags={tag}' for tag in tags)
    return '?'.join((url, url_params))


@register.simple_tag
def check_subscribe(user, author):
    # return Follow.objects.filter(user=user, author=author).exists()
    return user.follower.filter(author=author).exists


@register.simple_tag
def check_favorite(user, recipe_id):
    return user.favorite.filter(id=recipe_id).exists()


@register.simple_tag
def check_purchase(request, user, recipe_id):
    if user.is_authenticated:
        return user.basket.filter(id=recipe_id).exists()
    else:
        basket = request.session.get("basket")
        if basket is not None:
            return recipe_id in basket
        else:
            return 0


@register.simple_tag
def purchase_count(request):
    if request.user.is_authenticated:
        return request.user.basket.count()
    else:
        basket = request.session.get("basket")
        if basket is not None:
            return len(basket)
        return 0
