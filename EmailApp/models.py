from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import MEDIA_ROOT
# Create your models here.

fs = FileSystemStorage(location=MEDIA_ROOT+'EmailApp/attachments/')


class Attachments(models.Model):
    file = models.FileField(storage=fs)

    def __str__(self):
        return self.file.name
