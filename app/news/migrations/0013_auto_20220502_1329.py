# Generated by Django 3.2.9 on 2022-05-02 13:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_uk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Тело поста'),
        ),
    ]