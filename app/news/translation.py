from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'page_title', 'description', 'image')

translator.register(Blog, NewsTranslationOptions)
