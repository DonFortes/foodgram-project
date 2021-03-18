from django import forms

from .models import Recipe
from . import choices


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['ingredients', 'is_favorite', 'basket', 'author']
