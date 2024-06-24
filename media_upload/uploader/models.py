from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.docx', '.pptx', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class MediaFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
