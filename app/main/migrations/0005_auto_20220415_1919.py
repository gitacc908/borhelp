# Generated by Django 3.2.9 on 2022-04-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_landing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='landing',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='landing',
            name='description_ua',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='landing',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='landing',
            name='title_ua',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]