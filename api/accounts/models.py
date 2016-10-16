import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name,
                    is_staff=False, is_superuser=False, **extra_fields):
        """Create an user"""

        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name='', last_name='',
                         password=None, **extra_fields):
        """Create a super user"""

        return self.create_user(
            email, password,
            first_name,
            last_name,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class User(AbstractBaseUser):
    """Model that represents an user"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        """Unicode representation for an user model"""
        return self.email

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between"""
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        """Return the first_name"""
        return self.first_name
