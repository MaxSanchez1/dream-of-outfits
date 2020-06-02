from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("I 'c' an 'abc' in there silly guy")
        return title

