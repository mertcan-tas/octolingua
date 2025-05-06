from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from core.models import AbstractManager

class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, password=None, **extra_fields):        
        email = extra_fields.get("email")
        if email:
            extra_fields["email"] = self.normalize_email(email)
        
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser is_superuser=True'))

        return self.create_user(password, **extra_fields)
