from django.db import models
from shortuuid.django_fields import ShortUUIDField
from decouple import config, Csv
from versatileimagefield.fields import VersatileImageField
from django.core.validators import FileExtensionValidator
from core.utils import RandomFileName, validate_file_size
from django.utils import timezone

from account.models import User
from core.models import AbstractModel

class Profile(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    avatar = VersatileImageField(
        'avatar',
        null=True,
        blank=True,
        upload_to=RandomFileName('avatars/'),
        validators=[FileExtensionValidator(allowed_extensions=config('ALLOWED_IMAGE_TYPES', cast=Csv())), validate_file_size],
    )
    
    about = models.TextField(max_length=500, blank=True)

    experience_points = models.PositiveIntegerField(default=0)
    streak_days = models.PositiveIntegerField(default=0)
    streak_last_updated = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.email

    @property
    def full_name(self):
        return f"{self.name} {self.surname}".strip()

    @property
    def display_name(self):
        return f"{self.name} {self.surname}".strip()

    @property
    def has_avatar(self):
        return bool(self.avatar)
    
    @property
    def has_about(self):
        return bool(self.about.strip())

    @property
    def valid_name(self):
        return all([self.name.strip(), self.surname.strip()])

    def update_streak(self):
        """Kullanıcının günlük streak'ini günceller"""
        today = timezone.now().date()
        yesterday = today - timezone.timedelta(days=1)

        if self.streak_last_updated == yesterday:
            self.streak_days += 1
        elif self.streak_last_updated != today:
            self.streak_days = 1

        self.streak_last_updated = today
        self.save()