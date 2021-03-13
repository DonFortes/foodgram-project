from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import JsonResponse


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


def purchases(request):

    return JsonResponse({'success': 'true'})


def subscriptions(request):

    return JsonResponse({'success': 'true'})


def favorites(request):

    return JsonResponse({'success': 'true'})
