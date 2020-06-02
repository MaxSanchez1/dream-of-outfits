from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title Here"}))

    class Meta:
        model = Product
        fields = ['title',
                  'description',
                  'price'
                  ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "Astralis" not in title:
    #         raise forms.ValidationError("This is a loser title! :<")
    #     else:
    #         return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title Here"}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField()
