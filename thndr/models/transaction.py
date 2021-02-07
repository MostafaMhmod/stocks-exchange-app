from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    created_at = models.DateTimeField(("created_at"), auto_now_add=True)

    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)

    stock = models.ForeignKey('thndr.Stock', verbose_name=("stock"), null=True,
                              blank=True, on_delete=models.CASCADE)

    amount = models.IntegerField("amount", null=True, blank=True)
    stocks_total = models.IntegerField("total stocks", null=True, blank=True)

    deposit = models.BooleanField("deposit", null=False, blank=False)
    withdraw = models.BooleanField("withdraw", null=False, blank=False)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
