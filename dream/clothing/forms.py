from django import forms

from .models import Outfit
from .models import Article
from .models import Collection


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
        # these lines only allow the user's own articles to be selected
        self.fields['top'] = forms.ModelChoiceField(
            queryset=Article.objects.filter(creator=self.creator).filter(actual_location='TOP'))
        self.fields['bottom'] = forms.ModelChoiceField(
            queryset=Article.objects.filter(creator=self.creator).filter(actual_location='BTM'))
        self.fields['shoes'] = forms.ModelChoiceField(
            queryset=Article.objects.filter(creator=self.creator).filter(actual_location='SHS'))


class ArticleModelForm(forms.ModelForm):
    creator = None

    class Meta:
        model = Article
        fields = ['actual_location',
                  'clothing_type',
                  'color',
                  'cut',
                  'pattern',
                  'material',
                  ]

    def save(self):
        # use the automatically assigned fields that get data from the form
        obj = super(ArticleModelForm, self).save(commit=False)
        # set the creator as the user that submitted the page
        obj.creator = self.creator
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('user', None)
        super(ArticleModelForm, self).__init__(*args, **kwargs)


class CollectionModelForm(forms.ModelForm):
    creator = None

    # only going to allow name assignment on creation because articles and outfits
    # are to be added in the Collection detail page instead of this form
    class Meta:
        model = Collection
        fields = ['name']

    def save(self):
        # use the automatically assigned fields that get data from the form
        obj = super(CollectionModelForm, self).save(commit=False)
        # set the creator as the user that submitted the page
        obj.creator = self.creator
        obj.save()
        return obj

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('user', None)
        super(CollectionModelForm, self).__init__(*args, **kwargs)


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['articles']

    # I may have to override save to make the article stick but I'm honestly not sure
    # I will test without and see what happens


class AddOutfitForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['outfits']

    # I may have to override save to make the article stick but I'm honestly not sure
    # I will test without and see what happens
