from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def clean_servings(self):
        value = self.cleaned_data.get("servings")
        print(value)
        if value < 1:
            raise forms.ValidationError("The number of servings must be greater than zero.")
        return value