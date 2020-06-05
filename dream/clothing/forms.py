from django import forms

from .models import Outfit


class OutfitModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Outfit Title"}))

    class Meta:
        model = Outfit
        fields = ['title',
                  'top',
                  'bottom',
                  'shoes',
                  # 'jacket',
                  # 'socks',
                  # 'hat',
                  ]
