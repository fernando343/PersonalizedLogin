from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.


class User(AbstractUser):
    email = models.EmailField('email address', unique=True, error_messages={
        'unique': 'Este email ya esta en uso'
    })
    phone_regex = RegexValidator(
        regex=r'\+?1?\{9,15}$',
        message='Phone number must be enterd in the formar +9999999999'
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    is_client = models.BooleanField(
        'client status',
        default=True
    )
    is_verfied = models.BooleanField(
        'verified',
        default=False
    )

    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username