from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"),
                                on_delete=models.CASCADE, unique=True)

    # Money Fields SHOULD be a DecimalField but for simplicity we used PositiveIntegerField here
    balance = models.PositiveIntegerField('balance', default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
