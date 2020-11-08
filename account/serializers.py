from rest_framework import serializers
from account.models import Account

class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        field = '__all__'