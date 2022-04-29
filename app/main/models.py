from django.db import models
from ckeditor.fields import RichTextField


class Landing(models.Model):
    title = RichTextField(max_length=255, verbose_name='Заголовок')
    # image = models.ImageField(upload_to='page/', verbose_name='Изображение')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
