from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=settings.MEDIA_ROOT +"/user_datas/", blank=True)

    def name(self):
        return self.name.replace('media/user_data/', '')
