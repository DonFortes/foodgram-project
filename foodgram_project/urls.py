from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

handler404 = 'foodgram_project.views.page_not_found'
handler500 = 'foodgram_project.views.server_error'

urlpatterns = [
    path('', include('dishes.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/', include('api.urls')),
]
