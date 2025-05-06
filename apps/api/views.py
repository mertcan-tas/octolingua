from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count, Sum, Q

from api.models import (
    Language, Course, Skill, Lesson, Exercise, Answer,
    UserCourseProgress, UserSkillProgress,
    UserLessonProgress, UserExerciseAttempt
)
from account.serializers import ProfileSerializer
from account.models import Profile

from api.serializers import (
    LanguageSerializer, CourseListSerializer, CourseDetailSerializer,
    SkillSerializer, LessonSerializer, ExerciseSerializer,
    UserCourseProgressSerializer, UserSkillProgressSerializer,
    UserLessonProgressSerializer, UserExerciseAttemptSerializer,
    SubmitAnswerSerializer
)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


# Language Views
class LanguageListView(APIView):
    """Get all languages"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        languages = Language.objects.filter(is_active=True)
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)


class LanguageDetailView(APIView):
    """Get language details"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        language = get_object_or_404(Language, pk=pk, is_active=True)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)


# Course Views
class CourseListView(APIView):
    """Get all courses"""
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        courses = Course.objects.filter(is_published=True)
        
        # Filter by language if specified
        source_lang = request.query_params.get('source_language')
        target_lang = request.query_params.get('target_language')
        
        if source_lang:
            courses = courses.filter(source_language__code=source_lang)
        if target_lang:
            courses = courses.filter(target_language__code=target_lang)
            
        # Search functionality
        search = request.query_params.get('search')
        if search:
            courses = courses.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search)
            )
        
        # Apply pagination
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(courses, request)
        
        serializer = CourseListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CourseDetailView(APIView):
    """Get course details with all skills"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk, is_published=True)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)


class CourseEnrollView(APIView):
    """Enroll in a course"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk, is_published=True)
        user = request.user
        
        progress, created = UserCourseProgress.objects.get_or_create(
            user=user,
            course=course,
            defaults={'is_enrolled': True}
        )
        
        if not created and not progress.is_enrolled:
            progress.is_enrolled = True
            progress.save()
            
        return Response({'status': 'enrolled'}, status=status.HTTP_200_OK)


class CourseUnenrollView(APIView):
    """Unenroll from a course"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk, is_published=True)
        user = request.user
        
        try:
            progress = UserCourseProgress.objects.get(user=user, course=course)
            progress.is_enrolled = False
            progress.save()
            return Response({'status': 'unenrolled'}, status=status.HTTP_200_OK)
        except UserCourseProgress.DoesNotExist:
            return Response({'error': 'Not enrolled in this course'}, 
                            status=status.HTTP_400_BAD_REQUEST)


# Skill Views
class SkillListView(APIView):
    """Get all skills for a course"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk):
        skills = Skill.objects.filter(
            course_id=course_pk,
            is_published=True
        ).order_by('order')
        
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)


class SkillDetailView(APIView):
    """Get skill details with all lessons"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk, pk):
        skill = get_object_or_404(
            Skill, 
            pk=pk,
            course_id=course_pk,
            is_published=True
        )
        
        serializer = SkillSerializer(skill)
        return Response(serializer.data)


# Lesson Views
class LessonListView(APIView):
    """Get all lessons for a skill"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk, skill_pk):
        lessons = Lesson.objects.filter(
            skill_id=skill_pk,
            skill__course_id=course_pk
        ).order_by('order')
        
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonDetailView(APIView):
    """Get lesson details with all exercises"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk, skill_pk, pk):
        lesson = get_object_or_404(
            Lesson,
            pk=pk,
            skill_id=skill_pk,
            skill__course_id=course_pk
        )
        
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)


class LessonStartView(APIView):
    """Mark a lesson as started"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, course_pk, skill_pk, pk):
        lesson = get_object_or_404(
            Lesson,
            pk=pk,
            skill_id=skill_pk,
            skill__course_id=course_pk
        )
        user = request.user
        
        progress, created = UserLessonProgress.objects.get_or_create(
            user=user,
            lesson=lesson,
            defaults={'attempts': 1}
        )
        
        if not created:
            progress.attempts += 1
            progress.save()
            
        return Response({'status': 'lesson started'}, status=status.HTTP_200_OK)


class LessonCompleteView(APIView):
    """Mark a lesson as completed"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, course_pk, skill_pk, pk):
        lesson = get_object_or_404(
            Lesson,
            pk=pk,
            skill_id=skill_pk,
            skill__course_id=course_pk
        )
        user = request.user
        score = request.data.get('score', lesson.xp_reward)
        
        progress, created = UserLessonProgress.objects.get_or_create(
            user=user,
            lesson=lesson,
            defaults={
                'completed': True, 
                'score': score,
                'completed_at': timezone.now()
            }
        )
        
        if not created:
            progress.completed = True
            progress.score = score
            progress.completed_at = timezone.now()
            progress.save()
        
        # Update user's XP points
        profile = user.profile
        profile.experience_points += score
        profile.update_streak()
        profile.save()
        
        # Update skill progress
        skill_progress, _ = UserSkillProgress.objects.get_or_create(
            user=user,
            skill=lesson.skill
        )
        
        # Calculate progress percentage based on completed lessons
        total_lessons = lesson.skill.lessons.count()
        completed_lessons = UserLessonProgress.objects.filter(
            user=user,
            lesson__skill=lesson.skill,
            completed=True
        ).count()
        
        skill_progress.progress = completed_lessons / total_lessons
        
        if skill_progress.progress >= 1.0:
            skill_progress.completed = True
            skill_progress.level += 1
        
        skill_progress.save()
            
        return Response({
            'status': 'lesson completed',
            'xp_earned': score,
            'total_xp': profile.experience_points,
            'streak_days': profile.streak_days
        }, status=status.HTTP_200_OK)


# Exercise Views
class ExerciseListView(APIView):
    """Get all exercises for a lesson"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk, skill_pk, lesson_pk):
        exercises = Exercise.objects.filter(
            lesson_id=lesson_pk,
            lesson__skill_id=skill_pk,
            lesson__skill__course_id=course_pk
        ).order_by('order')
        
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)


class ExerciseDetailView(APIView):
    """Get exercise details"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, course_pk, skill_pk, lesson_pk, pk):
        exercise = get_object_or_404(
            Exercise,
            pk=pk,
            lesson_id=lesson_pk,
            lesson__skill_id=skill_pk,
            lesson__skill__course_id=course_pk
        )
        
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)


class ExerciseSubmitAnswerView(APIView):
    """Submit an answer to an exercise"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, course_pk, skill_pk, lesson_pk, pk):
        exercise = get_object_or_404(
            Exercise,
            pk=pk,
            lesson_id=lesson_pk,
            lesson__skill_id=skill_pk,
            lesson__skill__course_id=course_pk
        )
        user = request.user
        
        serializer = SubmitAnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        answer_given = serializer.validated_data['answer']
        
        # Check if answer is correct
        if exercise.type == 'MC':  # Multiple choice
            is_correct = Answer.objects.filter(
                exercise=exercise,
                id=answer_given,
                is_correct=True
            ).exists()
        else:
            # For simple text comparison (can be improved for translation exercises)
            correct_answers = Answer.objects.filter(
                exercise=exercise,
                is_correct=True
            ).values_list('text', flat=True)
            
            # Case insensitive comparison
            is_correct = answer_given.lower().strip() in [a.lower().strip() for a in correct_answers]
        
        # Save the attempt
        attempt = UserExerciseAttempt.objects.create(
            user=user,
            exercise=exercise,
            answer_given=answer_given,
            is_correct=is_correct
        )
        
        # Return result with correct answer if wrong
        result = {
            'is_correct': is_correct,
        }
        
        if not is_correct:
            # Only return correct answers for multiple choice
            if exercise.type == 'MC':
                correct_answers = Answer.objects.filter(
                    exercise=exercise, 
                    is_correct=True
                ).values('id', 'text')
                result['correct_answers'] = list(correct_answers)
        
        return Response(result, status=status.HTTP_200_OK)



class UserUpdateStreakView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.update_streak()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


# User Progress Views
class UserCourseProgressListView(APIView):
    """Get all user course progress"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        progress = UserCourseProgress.objects.filter(
            user=request.user,
            is_enrolled=True
        ).select_related('course')
        
        serializer = UserCourseProgressSerializer(progress, many=True)
        return Response(serializer.data)


class UserSkillProgressListView(APIView):
    """Get all user skill progress for a course"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, course_pk):
        progress = UserSkillProgress.objects.filter(
            user=request.user,
            skill__course_id=course_pk
        ).select_related('skill')
        
        serializer = UserSkillProgressSerializer(progress, many=True)
        return Response(serializer.data)


class UserLessonProgressListView(APIView):
    """Get all user lesson progress for a skill"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, course_pk, skill_pk):
        progress = UserLessonProgress.objects.filter(
            user=request.user,
            lesson__skill_id=skill_pk,
            lesson__skill__course_id=course_pk
        ).select_related('lesson')
        
        serializer = UserLessonProgressSerializer(progress, many=True)
        return Response(serializer.data)


class UserStatisticsView(APIView):
    """Get user learning statistics"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        profile = user.profile
        
        # Get summary statistics
        total_xp = profile.experience_points
        streak_days = profile.streak_days
        
        # Course statistics
        enrolled_courses = UserCourseProgress.objects.filter(
            user=user, 
            is_enrolled=True
        ).count()
        
        # Lesson statistics
        completed_lessons = UserLessonProgress.objects.filter(
            user=user,
            completed=True
        ).count()
        
        # Exercise statistics
        exercise_attempts = UserExerciseAttempt.objects.filter(user=user).count()
        correct_answers = UserExerciseAttempt.objects.filter(
            user=user,
            is_correct=True
        ).count()
        
        accuracy = 0
        if exercise_attempts > 0:
            accuracy = (correct_answers / exercise_attempts) * 100
        
        # Recent activity
        recent_lessons = UserLessonProgress.objects.filter(
            user=user,
            completed=True
        ).order_by('-completed_at')[:5]
        
        recent_activity = []
        for progress in recent_lessons:
            recent_activity.append({
                'lesson_title': progress.lesson.title,
                'skill_name': progress.lesson.skill.name,
                'course_title': progress.lesson.skill.course.title,
                'score': progress.score,
                'completed_at': progress.completed_at
            })
        
        return Response({
            'total_xp': total_xp,
            'streak_days': streak_days,
            'enrolled_courses': enrolled_courses,
            'completed_lessons': completed_lessons,
            'exercise_attempts': exercise_attempts,
            'correct_answers': correct_answers,
            'accuracy_percentage': round(accuracy, 2),
            'recent_activity': recent_activity
        })