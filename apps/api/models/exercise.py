from django.db import models
from api.models import Lesson  # İlişkili modeli import ediyoruz

class ExerciseType(models.TextChoices):
    MULTIPLE_CHOICE = 'MC', 'Çoktan Seçmeli'
    TRANSLATION = 'TR', 'Çeviri'
    FILL_BLANK = 'FB', 'Boşluk Doldurma'
    LISTENING = 'LS', 'Dinleme'
    SPEAKING = 'SP', 'Konuşma'
    MATCHING = 'MT', 'Eşleştirme'
    WORD_BANK = 'WB', 'Kelime Bankası'

class Exercise(models.Model):
    """Derslerdeki alıştırmaları temsil eder"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='exercises')
    type = models.CharField(max_length=2, choices=ExerciseType.choices)
    question_text = models.TextField()
    instruction = models.CharField(max_length=255, blank=True)
    hint = models.CharField(max_length=255, blank=True)
    audio_url = models.URLField(blank=True, null=True)  # Dinleme egzersizleri için
    image_url = models.URLField(blank=True, null=True)  # Görsel egzersizler için
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lesson.title} - Exercise {self.order}"

    class Meta:
        ordering = ['lesson', 'order']

class Answer(models.Model):
    """Bir alıştırmanın olası yanıtlarını temsil eder"""
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{'✓' if self.is_correct else '✗'} {self.text}"