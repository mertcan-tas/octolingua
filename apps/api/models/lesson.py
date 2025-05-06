from django.db import models
from api.models import Skill 

class Lesson(models.Model):
    """Bir beceri içindeki dersleri temsil eder"""
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()
    xp_reward = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.skill.name} - {self.title}"

    class Meta:
        ordering = ['skill', 'order']
        unique_together = ('skill', 'order')