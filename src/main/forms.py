'''
Модуль с описанием форм в виде классов
'''
from django.forms import ModelForm, TextInput, Textarea
from main.models import Translate, Summary


class TranslateFrom(ModelForm):
    '''
    Класс для генерации формы Translate
    '''
    class Meta:
        model = Translate
        fields = ['translated_article']
        widgets = {
            'translated_article': Textarea(attrs={
                'placeholder':
                    'Вставьте сюда статью на английском, '
                    'которую нужно перевести',
                'class': 'form-control',
            })
        }
        labels = {
            'translated_article': 'Перевод Статьи'
        }


class SummaryForm(ModelForm):
    '''Класс для генерации формы Summary'''
    class Meta:
        model = Summary
        fields = ['summarize_article']
        widgets = {
            'summarize_article': Textarea(attrs={
                'placeholder':
                    'Вставьте сюда статью, '
                    'по которой хотите получить краткое содержание',
                'class': 'form-control',
            })
        }
        labels = {
            'summarize_article': 'Краткое содержание статьи'
        }
