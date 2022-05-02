# Generated by Django 3.2.9 on 2022-04-26 12:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220420_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_uk',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=ckeditor.fields.RichTextField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_uk',
            field=ckeditor.fields.RichTextField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]