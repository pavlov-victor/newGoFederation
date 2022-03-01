from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import AbstractModel


class User(AbstractModel, AbstractUser):
    """Пользователь приложения."""

    patronymic = models.CharField(
        'Отчетство',
        max_length=120,
        default='',
        blank=False
    )
    location = models.ForeignKey(
        'locations.Location',
        models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Локация'
    )
    birth_date = models.DateField(
        'Дата рождения',
        null=True,
        blank=False
    )
