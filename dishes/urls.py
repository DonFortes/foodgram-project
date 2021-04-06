from django.urls import path
from dishes import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        r'^tag/(?P<tag_slug>[-\w]+)/$', views.index, name='recipe_list_by_tag'
    ),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('follows/', views.follows, name='follows'),
    path('recipe/<slug:slug>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<slug:slug>/', views.single_recipe, name='single_recipe'),
    path('recipe/<slug:slug>/delete/', views.delete_recipe,
         name='delete_recipe'),
    path('author/<str:username>/', views.profile, name='profile'),
    path('favorite/', views.favorite, name='favorite'),
]
