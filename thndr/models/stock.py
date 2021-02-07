import uuid

from django.db import models
from datetime import datetime


class Stock(models.Model):
    stock_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, null=True, primary_key=True
    )
    name = models.CharField(("name"), max_length=128)

    # Money Fields SHOULD be a DecimalField but for simplicity we used PositiveIntegerField here
    price = models.PositiveIntegerField('price', default=0)

    quantity = models.IntegerField()
    created_at = models.DateTimeField(("created_at"), auto_now_add=True)
    modified_at = models.DateTimeField(('modified'), auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        create_operation = not self.pk

        if not create_operation:
            self.modified_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
