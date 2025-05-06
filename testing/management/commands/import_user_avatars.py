from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from urllib.parse import urljoin
import uuid
import random

from account.models import User

class Command(BaseCommand):
    help = 'Populates user avatars with random images from picsum.photos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force update even if avatar already exists',
        )

    def handle(self, *args, **options):        
        users = User.objects.filter(is_superuser=False)

        for user in users:
            # Eğer avatar zaten varsa ve force seçeneği yoksa atla
            if user.profile.avatar and not options['force']:
                self.stdout.write(self.style.WARNING(
                    f'Skipping user {user.profile.full_name} (avatar already exists)'
                ))
                continue

            try:
                image_url = "https://thispersondoesnotexist.com/"  

                # Resmi indir
                response = requests.get(image_url, stream=True)
                response.raise_for_status()

                # Avatar alanına kaydet
                filename = f"{str(uuid.uuid4())}.jpg"
                user.profile.avatar.save(
                    filename,
                    ContentFile(response.content),
                    save=True
                )

                self.stdout.write(self.style.SUCCESS(
                    f'✔ Successfully updated avatar for {user.profile.full_name}'
                ))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'Error processing {user.profile.full_name}: {str(e)}'
                ))

        self.stdout.write(self.style.SUCCESS(
            f'✔ Successfully processed {users.count()} users'
        ))