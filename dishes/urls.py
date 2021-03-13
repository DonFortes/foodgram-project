from django.urls import path
from dishes import views


# добавить путь с неймом home, на него идет успешный редирект из сеттинг
urlpatterns = [
    path("", views.index, name="index"),
    path("purchases/", views.purchases, name="purchases"),

]
