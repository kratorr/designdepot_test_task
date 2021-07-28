from django.db import models


from django.conf import settings


from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name='Тэг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    content = RichTextUploadingField(blank=True, verbose_name='Содержание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Категория',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


class Feedback(models.Model):
    email = models.EmailField(verbose_name='Электронный адрес')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )