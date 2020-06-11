from django import forms

from .models import Outfit
from .models import Article


class OutfitModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Outfit Title"}))
    creator = None

    class Meta:
        model = Outfit
        fields = ['title',
                  'top',
                  'bottom',
                  'shoes',
                  ]

    def save(self):
        # use the automatically assigned fields that get data from the form
        obj = super(OutfitModelForm, self).save(commit=False)
        # set the creator as the user that submitted the page
        obj.creator = self.creator
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('user', None)
        super(OutfitModelForm, self).__init__(*args, **kwargs)
        # self.fields['clothes'] = forms.ModelChoiceField(queryset=Article.objects.filter(creator=user))
