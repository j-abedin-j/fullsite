from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'body','cover_image', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title