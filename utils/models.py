from django.db import models
from jalali_date import datetime2jalali
from accounts.models import User
from labscience.settings import DATE_INPUT_FORMATS, TIME_INPUT_FORMATS
from django.utils.translation import gettext as _


class GeneralDateModel(models.Model):
    create_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True

    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )

    class Meta:
        abstract = True
        ordering = ['-create_at']

    def get_create_at_jalali(self):
        return datetime2jalali(self.create_at).strftime(f'{DATE_INPUT_FORMATS} - {TIME_INPUT_FORMATS}')

    def get_updated_at_jalali(self):
        return datetime2jalali(self.updated_at).strftime(f'{DATE_INPUT_FORMATS} - {TIME_INPUT_FORMATS}')

