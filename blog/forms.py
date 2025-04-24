from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Post, Tag


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


class CategoryForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
 
 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
    

class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        
    def clean_name(self):
        return self.cleaned_data['name'].lower()
        
        
        
            