from django.shortcuts import get_object_or_404, redirect, render, reverse


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