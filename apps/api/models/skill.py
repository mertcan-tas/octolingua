from django.db import models
from api.models import Course  # İlişkili modeli import ediyoruz

class Skill(models.Model):
    """Kurslardaki becerileri temsil eder (Duolingo'daki 'skill bubbles')"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)  # Icon identifier or class
    order = models.PositiveIntegerField()
    level = models.PositiveIntegerField(default=1)  # Zorluk seviyesi
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.title} - {self.name}"

    class Meta:
        ordering = ['course', 'order']
        unique_together = ('course', 'order')