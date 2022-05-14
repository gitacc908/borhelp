from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify 
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description_meta = models.CharField(max_length=255, verbose_name='Описание мета', null=True, blank=True)
    keywords_meta = models.CharField(max_length=255, verbose_name='Keywords мета', null=True, blank=True)
    page_title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    slug = models.SlugField(blank=True, unique=True)
    description = RichTextUploadingField(verbose_name='Описание')
    created = models.DateField(verbose_name='Создан')
    image = models.ImageField(upload_to='news/', verbose_name='Превью')
    image2 = models.ImageField(upload_to='news/', verbose_name='Изображение', blank=True, null=True)
    viewed = models.PositiveSmallIntegerField(default=0, verbose_name='Просмотрено', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'News'
        verbose_name_plural = 'News'
