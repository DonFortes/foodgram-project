from django import forms

from .models import Recipe

# from . import choices


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['author', 'ingredients',
                   'is_favorite', 'shoplist', 'tags', ]
        widgets = {'tags': forms.CheckboxSelectMultiple()}
