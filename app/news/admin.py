from django.contrib import admin
from .models import Blog
from modeltranslation.admin import TranslationAdmin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        # fiedls = ['description']
        fields = '__all__'


# @admin.register(Blog)
class NewsAdmin(TranslationAdmin):
    # form = BlogForm
    list_display = ['title', 'created', 'description']
    list_search = ['title',]


admin.site.register(Blog, NewsAdmin)
