from uuid import uuid4

from django.db import models


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name='UUID4'
    )

    class Meta:
        abstract = True
        ordering = ('uuid',)


class AbstractTimeTrackable(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        abstract = True
        ordering = ('created_at', 'updated_at')


class AbstractModel(AbstractTimeTrackable, AbstractUUID):
    class Meta:
        abstract = True
