from . import views
from django.urls import path

urlpatterns = [ 
    path("purchases/", views.purchases, name="purchases"),
    path(
        "purchases/<int:recipe_id>/", views.purchases_remove,
        name="purchases_remove"
        ),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path(
        "subscriptions/<int:user_id>/", views.subscriptions,
        name="subscriptions"
        ),
    path("favorites/", views.favorites, name="favorites"),
    path(
        "favorites/<int:recipe_id>/", views.favorites_remove,
        name="favorites_remove"
        ),
    path("ingredients/", views.ingredients, name="ingredients"),
]
