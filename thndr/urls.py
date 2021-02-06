from django.contrib import admin
from django.urls import path

from thndr.api.deposit import deposit
from thndr.api.withdraw import withdraw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposit/', deposit, name="account-deposit"),
    path('withdraw/', withdraw, name="account-withdraw"),
]
