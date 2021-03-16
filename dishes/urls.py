from django.urls import path
from dishes import views


# добавить путь с неймом home, на него идет успешный редирект из сеттинг
urlpatterns = [
    path("", views.index, name="index"),
    path("purchases/", views.purchases, name="purchases"),

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
