from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = RichTextField(max_length=255, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Тело поста')
    created = models.DateTimeField(verbose_name='Создан')
    image = models.ImageField(upload_to='news/', verbose_name='Превью')
    viewed = models.PositiveSmallIntegerField(default=0, verbose_name='Просмотрено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
