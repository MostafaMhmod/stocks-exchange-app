from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    created_at = models.DateTimeField(("created_at"), auto_now_add=True)

    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)

    stock = models.OneToOneField('thndr.Stock', verbose_name=("stock"), null=True,
                                 blank=True, on_delete=models.CASCADE)

    amount = models.IntegerField("amount", editable=False)

    is_wallet = models.BooleanField("wallet_transaction", null=False, blank=False)
    is_stock = models.BooleanField("stock_transaction", null=False, blank=False)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
