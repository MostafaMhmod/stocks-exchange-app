from rest_framework import serializers

from django.contrib.auth.models import User


class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'email', 'username')
