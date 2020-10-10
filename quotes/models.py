from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django.utils.translation import ugettext_lazy as _

from quotes.enums import QuoteType


class Author(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField(_('text'), blank=False, null=False)
    author = models.ForeignKey('quotes.Author', null=True, on_delete=models.CASCADE)
    quote_type = models.CharField(_('type'), max_length=30, blank=False, null=False, choices=QuoteType.choices)

    class Meta:
        indexes = (
            HashIndex(fields=('quote_type',)),
        )
        verbose_name = _('quote')
        verbose_name_plural = _('quotes')

    @property
    def perex(self):
        perex = self.text[:30]
        return perex if len(self.text) <= 30 else perex + '...'

    def __str__(self):
        return _('Quote: {} by {}'.format(self.perex))
