from django.contrib import admin
from apps.main.models import Landing
from django import forms
from ckeditor.widgets import CKEditorWidget
from modeltranslation.admin import TranslationAdmin


class LandingForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Landing
        fields = ['title', 'image', 'description']


@admin.register(Landing)
class LandingAdmin(TranslationAdmin):
    form = LandingForm
    list_display = ['title', 'image', 'description']
    list_display_links = ['title']
    list_search = ['title']
