from django.contrib import admin

from thndr.models import Account, Stock, Wallet


class AccountAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ("id", 'user', "quantity",)


class StockAdmin(admin.ModelAdmin):
    search_fields = ("id", 'stock_uuid')
    list_display = ("id", 'stock_uuid', 'name', "price", "quantity",
                    "created_at", "modified_at",)


class WalletAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ("id", 'user', "balance",)


admin.site.register(Account, AccountAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Wallet, WalletAdmin)
