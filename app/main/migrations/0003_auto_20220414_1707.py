# Generated by Django 3.2.9 on 2022-04-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_page_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='Landing',
        ),
        migrations.AlterModelOptions(
            name='landing',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
    ]
