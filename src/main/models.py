"""
Модуль содержит классы моделей реализованных в приложении форм.
"""
from django.db import models
# Create your models here.


class Translate(models.Model):
    '''
    Модель формы Translate
    '''
    translated_article = models.TextField()


class Summary(models.Model):
    '''
    Модель формы Summary
    '''
    summarize_article = models.TextField()
