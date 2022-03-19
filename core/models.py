from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from .constants import IRANIAN_PHONE_NUMBER_REGEX_PATTERN


class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Payment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Document(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Ticket(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    phone_regex = RegexValidator(regex=IRANIAN_PHONE_NUMBER_REGEX_PATTERN,
                                 message="Phone number must be entered in the format: '09121234567'. 11 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=11, unique=True)  # validators should be a list

    first_name = models.CharField(
        _("first name"), max_length=150, null=False, blank=False)
    last_name = models.CharField(
        _("last name"), max_length=150, null=False, blank=False)
    address = models.TextField(blank=True)

    is_email_validated = models.BooleanField(default=False, null=False)
    is_phone_number_validated = models.BooleanField(default=False, null=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']  # adding phone_number here cause an error in createsuperuser command

    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = 'phone_number'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
