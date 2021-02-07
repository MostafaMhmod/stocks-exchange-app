from django.contrib import admin

from thndr.models import Transaction, Stock


class StockAdmin(admin.ModelAdmin):
    search_fields = ('stock_uuid',)
    list_display = ('stock_uuid', 'name', "price", "quantity",
                    "created_at", "modified_at",)


class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ('created_at', 'user', 'stock', 'amount',
                    'stocks_total', 'withdraw', 'deposit')


admin.site.register(Stock, StockAdmin)
admin.site.register(Transaction, TransactionAdmin)
