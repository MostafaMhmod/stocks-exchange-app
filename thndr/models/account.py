from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(
        User, verbose_name=("user"), on_delete=models.CASCADE, unique=True
    )
    balance = models.PositiveIntegerField('balance', default=0)

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
