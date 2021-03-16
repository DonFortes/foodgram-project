from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Follow, Shop_list, User, Recipe


def index(request):
    # post_list = Post.objects.all()
    # paginator = Paginator(post_list, 10)
    # page_number = request.GET.get('page')
    # page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {
            # 'page': page, 'paginator': paginator
            }
    )


@login_required
def purchases(request):
    user = request.user
    recipe_id = int(json.loads(request.body).get('id'))
    Shop_list.objects.create(
        user=user,
        recipe_id=recipe_id,
    )
    return JsonResponse({'success': 'true'})


@login_required
def shop_list(request):

    return render(
        request,
        'shop_list.html',
        {

        }
    )


@login_required
def subscriptions(request):

    return JsonResponse({'success': 'true'})


@login_required
def favorites(request):

    return JsonResponse({'success': 'true'})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipe = author.recipe.all()
    paginator = Paginator(recipe, 10)
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
        'index.html',
        {'page': page, 'paginator': paginator, 'author': author}
    )


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    user = request.user
    redirect_url = reverse("profile", args=[username])
    if author != user:
        Follow.objects.get_or_create(
            user=user,
            author=author,
        )
    return redirect(redirect_url)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    user = request.user
    Follow.objects.filter(user=user, author=author).delete()
    redirect_url = reverse("profile", args=[username])
    return redirect(redirect_url)
