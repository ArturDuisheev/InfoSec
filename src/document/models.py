import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from .services.path import path_document
from .services.slug import unique_slugify

from base.models import BaseModel


class Departament(BaseModel):
    title = models.CharField(
        _('Название департамента'),
        max_length=120
    )
    slug = models.CharField(
        _('Альт.название'),
        max_length=120,
        blank=True,
        unique=True
    )

    def __str__(self):
        return f'департамент: {self.title}'

    def get_absolute_url(self):
        return reverse('departament-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self.title)

        super().save(*args, **kwargs)


class Document(BaseModel):
    number = models.IntegerField(
        _('Номер документа')
    )
    name = models.CharField(
        _('Наименование документа'),
        max_length=120
    )

    document = models.FileField(
        _('Документ'),
        upload_to=path_document,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['docx', 'doc', 'pdf']
            )
        ]
    )

    departament = models.ForeignKey(
        Departament,
        on_delete=models.SET_NULL,
        null=True,
        related_name='document_of_departament',
        db_column='departament'
    )

    def __str__(self):
        return f'номер: {self.number}, название: {self.name}, {self.departament} создано в: {self.created_at}'

    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')
        db_table = 'documents'
