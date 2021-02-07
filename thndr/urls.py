from django.contrib import admin
from django.urls import path

from thndr.api.deposit import deposit
from thndr.api.withdraw import withdraw
from thndr.api.buy import buy
from thndr.api.sell import sell
from thndr.api.stock import stock
from thndr.api.user import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposit/', deposit, name="account-deposit"),
    path('withdraw/', withdraw, name="account-withdraw"),
    path('buy/', buy, name="stock-buy"),
    path('sell/', sell, name="stock-sell"),
    path('stock/', stock, name="stock"),
    path('user/', user, name="user"),
]
