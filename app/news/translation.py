from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'page_title', 'description', 'description_meta', 'keywords_meta', 'image')

translator.register(Blog, NewsTranslationOptions)
