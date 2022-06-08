from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'slug': forms.HiddenInput,
        }
