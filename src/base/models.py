import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    ID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        _('Создано в: '),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Обновлено в: '),
        auto_now=True
    )

    class Meta:
        abstract = True
