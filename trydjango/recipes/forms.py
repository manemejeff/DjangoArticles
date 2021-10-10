from django import forms

from .models import Recipe

class RecipeForm(forms.Form):
   class Meta:
       model = Recipe
       fields = [
           'name',
           'description',
           'directions'
       ]