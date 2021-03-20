from api import views
from django.urls import path


urlpatterns = [
    path('purchases/', views.purchases, name='purchases'),
    path(
        'purchases/<int:recipe_id>/', views.purchases,
        name='purchases_delete'
        ),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path(
        'subscriptions/<int:user_id>/', views.subscriptions,
        name='subscriptions_delete'
        ),
    path('favorites/', views.favorites, name='favorites'),
    path(
        'favorites/<int:recipe_id>/', views.favorites,
        name=f'avorites_delete'
        ),
    # path('ingredients/', views.ingredients, name='ingredients'),
]
