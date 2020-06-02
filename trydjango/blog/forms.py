from django import forms
from .models import Article


# NOTE: to use the title as a url, each one has to be unique. Add some sort of validation here.

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='', widget=forms.TextInput(
            attrs={"placeholder": "Title of Your Blog Article"}))

    class Meta:
        model = Article
        fields = [
            'title',
            'date',
            'content',
        ]
