# Generated by Django 3.2.9 on 2022-05-06 19:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220503_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_uk',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
