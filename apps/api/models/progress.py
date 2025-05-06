from django.db import models
from account.models import User  # İlişkili modeli import ediyoruz
from api.models import Course, Skill, Lesson, Exercise
from django.utils import timezone

class UserCourseProgress(models.Model):
    """Kullanıcıların kurs ilerleme durumunu izler"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField(default=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

    class Meta:
        unique_together = ('user', 'course')

class UserSkillProgress(models.Model):
    """Kullanıcıların beceri ilerleme durumunu izler"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill_progress')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)  # Kullanıcının beceri seviyesi
    progress = models.FloatField(default=0)  # 0-1 arasında ilerleme yüzdesi
    completed = models.BooleanField(default=False)
    last_practiced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"

    class Meta:
        unique_together = ('user', 'skill')

class UserLessonProgress(models.Model):
    """Kullanıcıların ders ilerleme durumunu izler"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    attempts = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"

    class Meta:
        unique_together = ('user', 'lesson')

class UserExerciseAttempt(models.Model):
    """Kullanıcıların egzersiz denemelerini izler"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercise_attempts')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    answer_given = models.TextField()
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.id} - {'Correct' if self.is_correct else 'Incorrect'}"