from django.shortcuts import render


def page_not_found(request, exception):

    return render(
        request,
        'misc/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(request, 'misc/500.html', status=500)


def technology(request):
    return render(request, 'misc/technology.html')


def about_author(request):
    return render(request, 'misc/about_author.html')
