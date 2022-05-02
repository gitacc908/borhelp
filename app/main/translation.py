from modeltranslation.translator import translator, TranslationOptions
from .models import Landing


class LandingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Landing, LandingTranslationOptions)
