from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class NewsForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text',  'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст новости'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }