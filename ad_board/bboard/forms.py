from django.forms import ModelForm, TextInput, Textarea, DateTimeField
from .models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = "__all__"
        labels = {'title': 'Enter the title ',
                  'content': 'Enter full description',
                  'price': 'How much for it?',
                  'published': 'Date',
                  'category': 'Enter category'}

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'category': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            "published": DateTimeField(),
            "content": Textarea(attrs={'class': 'form-control', 'placeholder': 'Full text'}),
        }

