from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Makes all users admin users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-superusers',
            action='store_true',
            help='Skip users who are already superusers',
        )

    def handle(self, *args, **options):
        User = get_user_model()
        skip_superusers = options['skip_superusers']
        
        users = User.objects.all()
        if skip_superusers:
            users = users.filter(is_superuser=False)
        
        total_users = users.count()
        updated_users = 0
        
        for user in users:
            # Make the user a staff member (required to access admin)
            user.is_staff = True
            # Make the user a superuser (full admin privileges)
            user.is_superuser = True
            user.save()
            updated_users += 1
            self.stdout.write(f"Made user '{user.email}' an admin")
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully made {updated_users} out of {total_users} users admin users'
        ))