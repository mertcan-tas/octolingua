from django.db import models
from api.models import Language 

class Course(models.Model):
    """Bir dilden diğerine öğretilen kursları temsil eder (İngilizce'den Türkçe'ye)"""
    title = models.CharField(max_length=255)
    source_language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='source_courses')
    target_language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='target_courses')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.source_language.code} → {self.target_language.code})"

    class Meta:
        unique_together = ('source_language', 'target_language')