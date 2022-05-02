# Generated by Django 3.2.9 on 2022-05-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_news_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description_meta',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание мета'),
        ),
        migrations.AddField(
            model_name='news',
            name='keywords_meta',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords мета'),
        ),
        migrations.AddField(
            model_name='news',
            name='page_title',
            field=models.CharField(default='asd', max_length=255, verbose_name='Заголовок страницы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='page_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='news',
            name='page_title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
