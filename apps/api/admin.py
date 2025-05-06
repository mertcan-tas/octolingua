from django.contrib import admin

from api.models import (
    Language, Course, Skill, Lesson, Exercise, Answer,
    UserCourseProgress, UserSkillProgress,
    UserLessonProgress, UserExerciseAttempt
)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_language', 'target_language', 'is_published')
    list_filter = ('is_published', 'source_language', 'target_language')
    search_fields = ('title', 'description')
    inlines = [SkillInline]

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'order', 'level', 'is_published')
    list_filter = ('course', 'level', 'is_published')
    search_fields = ('name', 'description')
    inlines = [LessonInline]

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill', 'order', 'xp_reward')
    list_filter = ('skill__course', 'skill')
    search_fields = ('title', 'description')
    inlines = [ExerciseInline]

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'type', 'order')
    list_filter = ('type', 'lesson__skill__course', 'lesson__skill')
    search_fields = ('question_text', 'instruction')
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'exercise', 'is_correct')
    list_filter = ('is_correct', 'exercise__type')
    search_fields = ('text',)

@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'is_enrolled', 'enrolled_at', 'last_activity')
    list_filter = ('is_enrolled', 'course')
    search_fields = ('user__username',)

@admin.register(UserSkillProgress)
class UserSkillProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'level', 'progress', 'completed', 'last_practiced')
    list_filter = ('completed', 'skill__course')
    search_fields = ('user__username',)

@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'attempts', 'score', 'completed_at')
    list_filter = ('completed', 'lesson__skill__course')
    search_fields = ('user__username',)

@admin.register(UserExerciseAttempt)
class UserExerciseAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'is_correct', 'created_at')
    list_filter = ('is_correct', 'exercise__lesson__skill__course')
    search_fields = ('user__username', 'answer_given')
    readonly_fields = ('user', 'exercise', 'answer_given', 'is_correct', 'created_at')