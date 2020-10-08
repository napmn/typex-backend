from django.db import models
from django.utils.translation import ugettext_lazy as _


class QuoteType(models.TextChoices):
    KNOWN = ('KNOWN', _('Known'))
