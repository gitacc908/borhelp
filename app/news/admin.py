from django.contrib import admin
from .models import Blog
from modeltranslation.admin import TranslationAdmin
from django import forms
from ckeditor.widgets import CKEditorWidget



@admin.register(Blog)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'created']
    list_search = ['title', 'description']
