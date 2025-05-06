from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import termcolors

class Command(BaseCommand):
    help = "Automatically runs makemigrations for all apps in PROJECT_APPS"

    def handle(self, *args, **options):
        project_apps = getattr(settings, "PROJECT_APPS", [])
        
        if not project_apps:
            self.stdout.write(self.style.ERROR("PROJECT_APPS not found in settings!"))
            return
        
        # Process each app
        for app in project_apps:
            try:
                self.stdout.write(termcolors.make_style(fg="green")(f"Running makemigrations for {app}"))
                call_command('makemigrations', app)
                self.stdout.write(termcolors.make_style(fg="green")(f"Successfully created migrations for {app}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to create migrations for {app}: {str(e)}"))
                # Continue with next app instead of breaking
        
        self.stdout.write(termcolors.make_style(fg="green")("All makemigrations commands completed"))