from django import forms

from .models import Recipe
from . import choices


class PostForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'
        ingredients = forms.ChoiceField(choices.get_choices)
