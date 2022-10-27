from users import forms
from users.models import Experience
from django.db import models
from django.forms.models import ModelForm
from .models import Recipe, Review
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['owner', 'vote_total', 'vote_ratio']
        widgets = {
            'cuisine': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredients'].widget.attrs['placeholder'] = '''Ingredients must be added in this format
        Rice - 1kg
        Chilli Powder - 1tsp
        Turmeric - 2tsp
        Capsicum - 1
        Cabbage - 1/4 kg
        Egg - 3'''
        self.fields['title'].widget.attrs['placeholder'] = 'Recipe name'
        self.fields['description'].widget.attrs['placeholder'] = 'Short description about it'
        self.fields['procedure'].widget.attrs['placeholder'] = 'Step by step procedure'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        
        self.fields['body'].widget.attrs['class'] = 'input--textarea'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'}) 