from django.contrib import admin

from .models import Follow, Ingredient, Recipe, Tag, Volume

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Volume)
admin.site.register(Follow)
