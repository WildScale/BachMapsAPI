from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.conf import settings
from users.utils import import_callable

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))
