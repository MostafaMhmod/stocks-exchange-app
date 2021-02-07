from django.contrib import admin

from thndr.models import Holding, Stock, Wallet


class HoldingAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ("id", 'user', 'stock', "quantity",)


class StockAdmin(admin.ModelAdmin):
    search_fields = ("id", 'stock_uuid')
    list_display = ("id", 'stock_uuid', 'name', "price", "quantity",
                    "created_at", "modified_at",)


class WalletAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ("id", 'user', "balance",)


admin.site.register(Holding, HoldingAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Wallet, WalletAdmin)
