from rest_framework import serializers
from account.models import User

from api.models import (
    Language, Course, Skill, Lesson, Exercise, Answer,
    UserCourseProgress, UserSkillProgress,
    UserLessonProgress, UserExerciseAttempt
)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'code', 'flag_icon', 'is_active']

class CourseListSerializer(serializers.ModelSerializer):
    source_language = LanguageSerializer(read_only=True)
    target_language = LanguageSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'source_language', 'target_language', 
                 'description', 'image', 'is_published']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

class ExerciseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Exercise
        fields = ['id', 'type', 'question_text', 'instruction', 
                 'hint', 'audio_url', 'image_url', 'order', 'answers']
        
class LessonSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'order', 'xp_reward', 'exercises']

class SkillSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'icon', 'order', 
                 'level', 'is_published', 'lessons']

class CourseDetailSerializer(serializers.ModelSerializer):
    source_language = LanguageSerializer(read_only=True)
    target_language = LanguageSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'source_language', 'target_language', 
                 'description', 'image', 'is_published', 'skills']

class UserCourseProgressSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    
    class Meta:
        model = UserCourseProgress
        fields = ['id', 'course', 'is_enrolled', 'enrolled_at', 'last_activity']

class UserSkillProgressSerializer(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField()
    
    class Meta:
        model = UserSkillProgress
        fields = ['id', 'skill', 'level', 'progress', 'completed', 'last_practiced']
    
    def get_skill(self, obj):
        return {
            'id': obj.skill.id,
            'name': obj.skill.name,
            'icon': obj.skill.icon,
            'level': obj.skill.level,
        }

class UserLessonProgressSerializer(serializers.ModelSerializer):
    lesson = serializers.SerializerMethodField()
    
    class Meta:
        model = UserLessonProgress
        fields = ['id', 'lesson', 'completed', 'attempts', 'score', 'completed_at']
    
    def get_lesson(self, obj):
        return {
            'id': obj.lesson.id,
            'title': obj.lesson.title,
            'xp_reward': obj.lesson.xp_reward,
        }

class UserExerciseAttemptSerializer(serializers.ModelSerializer):
    exercise = serializers.SerializerMethodField()
    
    class Meta:
        model = UserExerciseAttempt
        fields = ['id', 'exercise', 'answer_given', 'is_correct', 'created_at']
    
    def get_exercise(self, obj):
        return {
            'id': obj.exercise.id,
            'type': obj.exercise.type,
            'question_text': obj.exercise.question_text,
        }

class SubmitAnswerSerializer(serializers.Serializer):
    exercise_id = serializers.IntegerField()
    answer = serializers.CharField()
    
    def validate_exercise_id(self, value):
        try:
            exercise = Exercise.objects.get(id=value)
            return value
        except Exercise.DoesNotExist:
            raise serializers.ValidationError("Exercise not found.")