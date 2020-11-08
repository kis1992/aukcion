from django.db import models
from django.conf import settings
import time

# Create your models here.
def upload_avatar(instance, filename):
    lastDot = filename.rfind('.')
    extension = filename[lastDot:len(filename):1]
    return 'images/user/%s-%s-%s' % (instance.user.username, time.time(), extension)

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to=upload_avatar)
    money = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
