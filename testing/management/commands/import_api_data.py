from django.core.management.base import BaseCommand
from account.models import User
from django.utils import timezone
from django.db import transaction

from api.models import (
    Language,
    Course,
    Skill,
    Lesson,
    Exercise,
    Answer,
    ExerciseType
)

class Command(BaseCommand):
    help = 'Populates the database with sample language learning data'


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate sample data...'))

        try:
            with transaction.atomic():
                # Create languages
                self.stdout.write('Creating languages...')
                turkish_lang = Language.objects.create(
                    name='Türkçe',
                    code='tr',
                    is_active=True
                )

                english_lang = Language.objects.create(
                    name='English',
                    code='en',
                    is_active=True
                )

                # Create a course
                self.stdout.write('Creating course "Türkçe\'den İngilizce\'ye"...')
                course = Course.objects.create(
                    title='Türkçe\'den İngilizce\'ye',
                    source_language=turkish_lang,
                    target_language=english_lang,
                    description='Türkçe konuşanlar için İngilizce kursu',
                    is_published=True
                )

                # Create skills (units)
                self.stdout.write('Creating skills...')
                skills = [
                    {
                        'name': 'Temel İfadeler',
                        'description': 'İngilizce\'de en çok kullanılan temel ifadeler',
                        'icon': 'chat',
                        'order': 1,
                        'level': 1
                    },
                    {
                        'name': 'Tanışma',
                        'description': 'Kendinizi tanıtmayı öğrenin',
                        'icon': 'person',
                        'order': 2,
                        'level': 1
                    },
                    {
                        'name': 'Yiyecekler',
                        'description': 'Yiyecek ve içecek isimleri',
                        'icon': 'food',
                        'order': 3,
                        'level': 1
                    }
                ]

                created_skills = []
                for skill_data in skills:
                    skill = Skill.objects.create(
                        course=course,
                        is_published=True,
                        **skill_data
                    )
                    created_skills.append(skill)

                # Create lessons for the first skill
                self.stdout.write('Creating lessons for the first skill...')
                lessons = [
                    {
                        'title': 'Selamlaşma',
                        'description': 'İngilizce\'de selamlaşma ifadeleri',
                        'order': 1,
                        'xp_reward': 10
                    },
                    {
                        'title': 'Teşekkür Etme',
                        'description': 'Teşekkür etme ve karşılık verme',
                        'order': 2,
                        'xp_reward': 10
                    }
                ]

                created_lessons = []
                for lesson_data in lessons:
                    lesson = Lesson.objects.create(
                        skill=created_skills[0],
                        **lesson_data
                    )
                    created_lessons.append(lesson)

                # Create exercises for the first lesson
                self.stdout.write('Creating exercises for the first lesson...')
                exercises = [
                    {
                        'type': ExerciseType.MULTIPLE_CHOICE,
                        'question_text': '"Merhaba" nasıl denir?',
                        'instruction': 'Doğru çeviriyi seçin',
                        'hint': 'En yaygın selamlaşma ifadesi',
                        'order': 1
                    },
                    {
                        'type': ExerciseType.TRANSLATION,
                        'question_text': '"Günaydın" İngilizce\'de nasıl söylenir?',
                        'instruction': 'Türkçe\'den İngilizce\'ye çevirin',
                        'hint': 'Sabah kullanılan selamlaşma ifadesi',
                        'order': 2
                    },
                    {
                        'type': ExerciseType.FILL_BLANK,
                        'question_text': '_____ evening! (İyi akşamlar!)',
                        'instruction': 'Boşluğu doldurun',
                        'hint': 'Akşam selamlaşması',
                        'order': 3
                    }
                ]

                created_exercises = []
                for exercise_data in exercises:
                    exercise = Exercise.objects.create(
                        lesson=created_lessons[0],
                        **exercise_data
                    )
                    created_exercises.append(exercise)

                # Create answers for the exercises
                self.stdout.write('Creating answers for the exercises...')

                # Answers for the first exercise (multiple choice)
                Answer.objects.create(
                    exercise=created_exercises[0],
                    text='Hello',
                    is_correct=True
                )
                Answer.objects.create(
                    exercise=created_exercises[0],
                    text='Goodbye',
                    is_correct=False
                )
                Answer.objects.create(
                    exercise=created_exercises[0],
                    text='Thank you',
                    is_correct=False
                )
                Answer.objects.create(
                    exercise=created_exercises[0],
                    text='Yes',
                    is_correct=False
                )

                # Answers for the second exercise (translation)
                Answer.objects.create(
                    exercise=created_exercises[1],
                    text='Good morning',
                    is_correct=True
                )
                Answer.objects.create(
                    exercise=created_exercises[1],
                    text='Morning',
                    is_correct=True  # Alternative correct answer
                )

                # Answers for the third exercise (fill in the blank)
                Answer.objects.create(
                    exercise=created_exercises[2],
                    text='Good',
                    is_correct=True
                )

            self.stdout.write(self.style.SUCCESS('Successfully populated sample data!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}'))
