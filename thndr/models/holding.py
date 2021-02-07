from django.contrib.auth.models import User
from django.db import models


class Holding(models.Model):
    user = models.OneToOneField(
        User, verbose_name=("user"), on_delete=models.CASCADE
    )
    stock = models.OneToOneField('thndr.Stock', verbose_name=("stock"), on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField('quantity', default=0)

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        return self.user.get_full_name()

    class Meta:
        unique_together = ('user', 'stock',)
        verbose_name = "Holding"
        verbose_name_plural = "Holdings"
