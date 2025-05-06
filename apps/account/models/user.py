from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from account.managers import UserManager
from django.conf import settings

from core.models import AbstractModel, AbstractManager

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, verbose_name="Email", unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    
    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.email