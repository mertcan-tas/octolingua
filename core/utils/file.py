import os
import uuid
from django.utils.deconstruct import deconstructible
from decouple import config
from django.core.exceptions import ValidationError

@deconstructible
class RandomFileName:
    def __init__(self, path):
        self.path = path
    
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4().hex}.{ext}'
        return os.path.join(self.path, filename)

def validate_file_size(value):
    max_size_mb = config('MAX_FILE_SIZE', default=3, cast=int)
    limit = max_size_mb * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f"File size should not exceed {max_size_mb} MB. Current size: {value.size / (1024 * 1024):.2f} MB.")