from django.urls import path
from dishes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<slug:slug>/', views.single_recipe, name='slug'),
    path('author/<str:username>/', views.profile, name='profile'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),

    path(
        '<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
        ),
    path(
        '<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
        ),
]
