# Generated by Django 3.2.9 on 2022-04-15 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220415_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='description_en_us',
        ),
        migrations.RemoveField(
            model_name='landing',
            name='description_uk',
        ),
    ]
