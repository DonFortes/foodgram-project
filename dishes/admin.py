from django.contrib import admin

from .models import Follow, Ingredient, Recipe, Tag, Volume


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('name',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Volume)
admin.site.register(Follow)
