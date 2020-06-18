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

    # this save should just add on one article to the list of articles
    def save(self, *args, **kwargs):
        # creates the new collection instance
        updated_instance = super(AddArticleForm, self).save(commit=False)
        print(updated_instance.articles.all())
        print(self.cleaned_data['articles'])
        updated_instance.articles.add(self.cleaned_data['articles'].first())
        updated_instance.save()


class AddOutfitForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['outfits']

    def save(self, *args, **kwargs):
        # creates the new collection instance
        updated_instance = super(AddOutfitForm, self).save(commit=False)
        print(updated_instance.outfits.all())
        print(self.cleaned_data['outfits'])
        updated_instance.outfits.add(self.cleaned_data['outfits'].first())
        updated_instance.save()
