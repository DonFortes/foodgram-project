from django import forms

from .models import Reciept
from . import choices


class PostForm(forms.ModelForm):
    class Meta:
        model = Reciept
        fields = '__all__'
        ingredients = forms.ChoiceField(choices.get_choices)
