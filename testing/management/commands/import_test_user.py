from django.core.management.base import BaseCommand
from django.utils import termcolors
from decouple import config
from faker import Faker
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
import sys
import time

class Command(BaseCommand):
    help = "Creates a test user with predefined data"
    
    def handle(self, *args, **options):
        fake = Faker('tr_TR')
        start = time.time()
        user_count = config('TESTING_USER_COUNT', cast=int, default=5)
        User = get_user_model()
        
        try:
            for _ in range(user_count):
                name = fake.first_name()
                surname = fake.last_name()
                email = f"{slugify(name.lower())}.{slugify(surname.lower())}@outlook.com"
                
                password = get_random_string(
                    length=12,
                    allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
                )
                
                # Create user instance without saving
                user = User(
                    email=email,
                    password=password 
                )
                user.set_password(password)  # Handles password hashing
                
                # Set temporary attributes
                user._name = name
                user._surname = surname
                
                user.save()  # Now the signal will have access to the attributes

            success_msg = termcolors.make_style(fg='green', opts=('bold',))(f'✔ {user_count} test user created successfully !\n')
            self.stdout.write(success_msg)
            
            self.stdout.write(termcolors.make_style(fg="cyan")(f'Time: {time.time() - start}'))
            
        except Exception as e:
            error_msg = termcolors.make_style(fg='red', opts=('blink',))(
                f'✘ Hata: {str(e)}'
            )
            self.stdout.write(error_msg)
            sys.exit(1)