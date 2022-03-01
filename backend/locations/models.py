from django.db import models

from utils.models import AbstractModel


class Location(AbstractModel):
    """Локации."""
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
