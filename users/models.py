from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    PASSWORD_MIN_SIZE = 5

    email = models.EmailField(_('email'), unique=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
