from django.db import models
from django.utils import timezone

from account.models import User

class AccountVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification')
    
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)

    phone_verified = models.BooleanField(default=False)
    phone_verified_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Account Verification'
        verbose_name_plural = 'Account Verifications'
    
    def __str__(self):
        return f"{self.user.email}'s Verification"

    def verify_email(self):
        self.email_verified = True
        self.email_verified_at = timezone.now()
        self.save()  

    def verify_phone(self):
        self.phone_verified = True
        self.phone_verified_at = timezone.now()
        self.save() 