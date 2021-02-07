from rest_framework import serializers

from django.contrib.auth.models import User
from thndr.utils.get_user_wallet_balance import get_user_wallet_balance


class UserRetreieveSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        return get_user_wallet_balance(obj.pk)

    class Meta:
        model = User
        fields = ('pk', 'email', 'username', 'balance')
