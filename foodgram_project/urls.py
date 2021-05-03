from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

from . import views

handler404 = 'foodgram_project.views.page_not_found'  # noqa
handler500 = 'foodgram_project.views.server_error'  # noqa

urlpatterns = [
    path('', include('dishes.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/', include('api.urls')),
    path('technology/', views.technology, name='technology'),
    path('about_author/', views.about_author, name='about_author'),

]
