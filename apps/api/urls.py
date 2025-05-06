from django.urls import path
from api.views import (
     LanguageListView,
     LanguageDetailView,
     CourseListView,
     CourseDetailView,
     CourseEnrollView,
     CourseUnenrollView,
     SkillListView,
     SkillDetailView,
     LessonListView,
     LessonDetailView,
     LessonStartView,
     LessonCompleteView,
     ExerciseListView,
     ExerciseDetailView,
     ExerciseSubmitAnswerView,
     UserUpdateStreakView,
     UserCourseProgressListView,
     UserSkillProgressListView,
     UserLessonProgressListView,
     UserStatisticsView,
)

urlpatterns = [
    # Language URLs
    path('languages/', LanguageListView.as_view(), name='language-list'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
    
    # Course URLs
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/enroll/', CourseEnrollView.as_view(), name='course-enroll'),
    path('courses/<int:pk>/unenroll/', CourseUnenrollView.as_view(), name='course-unenroll'),
    
    # Skills URLs
    path('courses/<int:course_pk>/skills/', SkillListView.as_view(), name='skill-list'),
    path('courses/<int:course_pk>/skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    
    # Lessons URLs
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/', 
         LessonListView.as_view(), name='lesson-list'),
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:pk>/', 
         LessonDetailView.as_view(), name='lesson-detail'),
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:pk>/start/', 
         LessonStartView.as_view(), name='lesson-start'),
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:pk>/complete/', 
         LessonCompleteView.as_view(), name='lesson-complete'),
    
    # Exercises URLs
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:lesson_pk>/exercises/', 
         ExerciseListView.as_view(), name='exercise-list'),
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:lesson_pk>/exercises/<int:pk>/', 
         ExerciseDetailView.as_view(), name='exercise-detail'),
    path('courses/<int:course_pk>/skills/<int:skill_pk>/lessons/<int:lesson_pk>/exercises/<int:pk>/submit/', 
         ExerciseSubmitAnswerView.as_view(), name='exercise-submit'),
    
    # User Profile URLs
    path('profile/update-streak/', UserUpdateStreakView.as_view(), name='update-streak'),
    
    # User Progress URLs
    path('progress/courses/', UserCourseProgressListView.as_view(), name='user-course-progress'),
    path('progress/courses/<int:course_pk>/skills/', 
         UserSkillProgressListView.as_view(), name='user-skill-progress'),
    path('progress/courses/<int:course_pk>/skills/<int:skill_pk>/lessons/', 
         UserLessonProgressListView.as_view(), name='user-lesson-progress'),
    path('statistics/', UserStatisticsView.as_view(), name='user-statistics'),
]