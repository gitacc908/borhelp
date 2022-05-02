from modeltranslation.translator import translator, TranslationOptions
from .models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'page_title', 'description', 'image')

translator.register(News, NewsTranslationOptions)