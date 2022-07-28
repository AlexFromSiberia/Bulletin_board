from django.forms import ModelForm, TextInput, Textarea, DateTimeField
from .models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = "__all__"
        labels = {'title': 'Enter the title ',
                  'content': 'Enter full description',
                  'price': 'How much for it?',
                  'category': 'Choose the category',
                  }

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your price in US dollars'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Full text'}),
        }

