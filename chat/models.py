from django.db import models
from account.models import Account
from lot.models import Lot

# Create your models here.
class Chat(models.Model):
    lot = models.ForeignKey(Lot,related_name='chats',on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    activity = models.BooleanField(default=True)
    user = models.OneToOneField(Account,on_delete = models.CASCADE)


