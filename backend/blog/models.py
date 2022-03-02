from django.db import models

from utils.models import AbstractModel


class BlogPost(AbstractModel):
    description = models.TextField(
        'Краткое описание для главной страницы',
    )
    body = models.TextField(
        'Текст поста',
    )
    author = models.ForeignKey(
        'users.User',
        models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Автор'
    )
    title = models.CharField(
        'Название поста',
        max_length=300
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'


class BlogComment(AbstractModel):
    post = models.ForeignKey(
        BlogPost,
        models.CASCADE,
        verbose_name='Пост'
    )
    author = models.ForeignKey(
        'users.User',
        models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return 'Комментарий от ' + self.author.__str__() if self.author else 'Анонима'

    class Meta:
        verbose_name = 'Комментарий блога'
        verbose_name_plural = 'Комментарии блога'


class BlogMenu(AbstractModel):
    is_active = models.BooleanField(
        'Активно',
        default=True
    )
    name = models.CharField(
        'Название меню',
        max_length=120
    )
    order = models.IntegerField(
        'Порядок элемента',
        default=1
    )
    link = models.TextField(
        'ссылка для переадресации'
    )
    parent = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'
        ordering = ['order']
