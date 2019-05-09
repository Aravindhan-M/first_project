from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .utils import get_mobile_operators
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = 'AD'
    TELECOM_USER = 'TU'
    END_USER = 'EU'
    ROLE_NAME = (
        (ADMIN, 'Administrator'),
        (TELECOM_USER, 'Telecom User'),
        (END_USER, 'End User'),
    )
    GENDER = (

        ("MALE","Male"),

        ("FEMALE","Female"),
        ("OTHERS","Others"),

    )
    MOBILE_OPERATORS = (

        ("OPERATOR1", "OPERATOR1"),

        ("OPERATOR2", "OPERATOR2"),
        ("OPERATOR3", "OPERATOR3"),

    )

    email = models.EmailField(_('Email address'),blank=True)
    mobile_number = models.CharField(_('Mobile number'), max_length=30,unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    date_of_birth = models.DateTimeField(_('Date of Birth'),blank=True,null=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active status'), default=True)
    is_staff = models.BooleanField(_('Staff status'), default=False)
    is_phone_verified = models.BooleanField(_('Mobile Verified Status'), default=False)
    is_email_verified = models.BooleanField(_('Email Verified Status'), default=False)
    role_name = models.CharField(max_length=2, choices=ROLE_NAME, default=END_USER, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    mobile_operator = models.CharField(max_length=60,choices=get_mobile_operators(), blank=True,null=True)
    accept_reject_info = models.TextField(max_length=300,blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'User'

    def __str__(self):
        return self.email

    def get_full_name(self):

        full_name = '%s' % (self.name)
        return full_name.strip()

    def get_short_name(self):
        return self.name

    @property
    def is_operator(self):
        return self.role_name == 'TU'
