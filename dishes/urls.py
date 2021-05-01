from django.urls import path

from dishes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('follows/', views.follows, name='follows'),
    path('recipe/<slug:slug>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<slug:slug>/', views.single_recipe, name='single_recipe'),
    path('recipe/<slug:slug>/delete/', views.delete_recipe,
         name='delete_recipe'),
    path('author/<str:username>/', views.profile, name='profile'),
    path('favorite/', views.favorite, name='favorite'),
    path('shoplist/', views.shoplist, name='shoplist'),
    path('put/', views.put_ingredients_into_base, name='put'),
    path('download_file/', views.download_file, name='download_file'),
]
