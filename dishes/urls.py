from django.urls import path
from dishes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("purchases/", views.purchases, name="purchases"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("subscriptions/<int:id>/", views.subscriptions, name="subscriptions"),
    path("favorites/", views.favorites, name="favorites"),


    path(
        "<str:username>/follow/",
        views.profile_follow,
        name="profile_follow"
        ),
    path(
        "<str:username>/unfollow/",
        views.profile_unfollow,
        name="profile_unfollow"
        ),
]
